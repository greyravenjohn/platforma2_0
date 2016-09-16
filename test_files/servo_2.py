#servoblaster
import os
import time

for x in range(5, 45):
    y = x*2
    os.system('echo 0=%(y)s' %locals() +'% > /dev/servoblaster' )
    time.sleep(0.05)

for x in reversed(range(10, 90)):
    os.system('echo 0=%(x)s' %locals() +'% > /dev/servoblaster' )
    time.sleep(0.025)
