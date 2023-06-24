from picamera import PiCamera
from time import sleep

camera = PiCamera()

# vidCycle sets the entire photo & video loop to happen 50 times starting at 1.
# seshPrefix sets a prefix (in 1000s) to indicate the time elapsed before this sesion.
# seshPrefix starts at 0 and adds 10,000 each cycle. 10,000 = 10 mins elapsed.

for vidCycle in range(1,51):
    camera.resolution = (1640, 1232)
    seshPrefix=(vidCycle-1)*10000
    vidNum=seshPrefix+vidCycle
    sleep(1)
    camera.start_recording('/home/pi/SkyOutVideos/habOutVid.%s.h264' % vidNum)
    sleep(59)
    camera.stop_recording()
    session=vidCycle*10000
    for picSesh in range(1,121):
        camera.resolution = (2592, 1944)
        sleep(5)
        picNum=seshPrefix+picSesh
        camera.capture('/home/pi/SkyOutImages/habOutPic.%s.jpg' % picNum)