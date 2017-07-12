#!/usr/bin/env python

import lightpack
from time import sleep
import sys

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

lp = lightpack.Lightpack( led_map=led_map, api_key=api_key )
try:
    lp.connect()
except lightpack.CannotConnectError as e:
    print repr(e)
    sys.exit(1)

# Lock the Lightpack so we can make changes
lp.lock()


for i in range(3):
    lp.setColourToAll((0, 255, 0))
    sleep( 0.2 )
    lp.setColourToAll((0, 0, 0))
    sleep( 0.2 )

print( lp.getProfiles() )

lp.unlock()

lp.disconnect()
