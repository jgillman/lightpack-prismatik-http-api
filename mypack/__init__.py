import lightpack
import sys
import time

class myPack:

    def __init__(self):
        # Configuration
        # host = 'localhost' # (default)
        # port = 3636 # (default)
        # api_key = '{YOUR-API-KEY-IF-USED}' # not used by default

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

        self.lp = lightpack.Lightpack( led_map=led_map, api_key=api_key )

        self.retry_counter = 0
        self.retry_limit = 120
        self.retry_interval = 5

    def connect(self):
        try:
            self.lp.connect()
            print 'Connected to Lightpack'
        except lightpack.CannotConnectError as e:
            if self.retry_counter < self.retry_limit:
                self.retry_connect()
            else:
                print 'Retry limit reached. Is Prismatik started with the API running?'
                print repr(e)
                sys.exit(1)

    def retry_connect(self):
        self.retry_counter += 1
        print "Lightpack unavailable, trying again in %s seconds..." % ( self.retry_interval )
        time.sleep( self.retry_interval )
        self.connect()


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
