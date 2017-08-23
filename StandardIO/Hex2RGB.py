#!/usr/bin/python

import sys, time

while True:

    print 'Enter color hex (e.g. #ff0000, #AABBCC):'
    sys.stdout.flush()
    h = raw_input().lstrip('#')
    print 'RGB = (%s, %s, %s)' %  tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    sys.stdout.flush()
    time.sleep(1)

