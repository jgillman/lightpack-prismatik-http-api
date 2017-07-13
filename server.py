#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import mypack

pack = mypack.myPack()

PORT_NUMBER = 8080

class myHandler( BaseHTTPRequestHandler ):

    def do_GET( self ):

        sendReply = False
        response = ''

        if self.path == '/lightpack':
            sendReply = True

        if self.path == '/lightpack/on':
            sendReply = True
            pack.on()

        if self.path == '/lightpack/off':
            sendReply = True
            pack.off()

        if self.path.startswith( '/lightpack/profile/' ):
            if pack.setProfile( self.path.split('/')[-1] ):
                sendReply = True

        if sendReply == True:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.sendPackStatusResponse()
        else:
            self.send_response(404)

        return

    def sendPackStatusResponse(self):
        response = "{ 'power': '" + pack.getStatus() + "', 'profile': '" + pack.getProfile() + "' }"
        self.wfile.write( response )


try:
    server = HTTPServer( ('', PORT_NUMBER), myHandler )
    print 'Started httpserver on port %d' % PORT_NUMBER
    pack.connect()
    server.serve_forever()

except KeyboardInterrupt:
    print '^C recieved, shutting down the web server'
    pack.disconnect()
    server.socket.close()


