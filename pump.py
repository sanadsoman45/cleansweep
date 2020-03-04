import time
import RPi.GPIO as gp
channel=7
print("before cleanup")
gp.cleanup()
print("after cleanup")
gp.setmode(gp.BOARD)
gp.setup(channel,gp.OUT)
try:
    print("hello z")
    gp.output(channel,True)
    time.sleep(10)
    gp.output(channel,False)
    gp.cleanup()
except:
    gp.cleanup()
print("success")
