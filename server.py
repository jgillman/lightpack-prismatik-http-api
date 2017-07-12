#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080

class myHandler( BaseHTTPRequestHandler ):

    def do_GET( self ):

        sendReply = False
        response = ''

        if self.path == '/lightpack':
            sendReply = True
            response = "{ 'power': '" + pack.getStatus() + "', 'profile': '" + pack.getProfile() + "' }"

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
            if response != '':
                self.wfile.write( response )
        else:
            self.send_response(404)

        return




import lightpack
import sys

class myPack:

    def __init__(self):
        # Configuration
        # host = 'localhost' # (default)
        # port = 3636 # (default)
        led_map = [ # Optional aliases for the LEDs in order
            'bottom-right',
            'right-bottom',
            'right-top',
            'top-far-right',
            'top-right',
            'top-left',
            'top-far-left',
            'left-top',
            'left-bottom',
            'bottom-left',
        ]
        api_key = '{e5ecc13c-45f3-4652-a0fb-b03eb07b894e}'
        self.lp = lightpack.Lightpack( led_map=led_map, api_key=api_key )

    def connect(self):
        try:
            self.lp.connect()
            print 'Connected to Lightpack'
        except lightpack.CannotConnectError as e:
            print repr(e)
            sys.exit(1)

    def disconnect(self):
        self.lp.disconnect()
        print 'Disconnected from Lightpack'

    def on(self):
        self.lp.lock();
        self.lp.turnOn();
        self.lp.unlock();

    def off(self):
        self.lp.lock();
        self.lp.turnOff();
        self.lp.unlock();

    def getStatus(self):
        return self.lp.getStatus()

    def getProfile(self):
        return self.lp.getProfile()

    def setProfile(self, profile):
        self.lp.lock()
        try:
            self.lp.setProfile( profile )
        except lightpack.CommandFailedError as e:
            print repr(e)
            print "Profile '%s' not found." % profile
            return False
        self.lp.unlock()
        return True


pack = myPack()

try:
    server = HTTPServer( ('', PORT_NUMBER), myHandler )
    print 'Started httpserver on port %d' % PORT_NUMBER
    pack.connect()
    server.serve_forever()

except KeyboardInterrupt:
    print '^C recieved, shutting down the web server'
    pack.disconnect()
    server.socket.close()


