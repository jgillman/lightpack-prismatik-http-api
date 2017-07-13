import lightpack
import sys

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
