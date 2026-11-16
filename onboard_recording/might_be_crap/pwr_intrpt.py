from time import sleep
from datetime import datetime
from picamera import PiCamera

#This is the initial step.
camera = PiCamera()

#For resolution and frame rate, there are trade-offs.

#If you want 60 fps, lower resolution:
camera.resolution = (1280, 720)
camera.framerate = 60

#If you want higher resolution, go down to 30 fps:
camera.resolution = (1920, 1080)
camera.framerate = 30

#Here is a basic loop to showcase the two video modes:
framerates=[60,30]
resolution = [(1280,720), (1920,1080)]
#output=['720.h264', '1080.h264']

def var_exists():
     exists = "t1_end" in locals() or "t1_end" in globals()
     return exists

for i in range(2):
    camera.resolution = resolution[i]
    camera.framerate = framerates[i]
    #print('Now doing '+output[i])
    t1_start = datetime.now()

    if var_exists():
        print('time since last vid is')
        print(t1_start - t1_end)
    else:
        print('first iteration')

    t2_start = t1_start.strftime("%m-%d-%Y_%H_%M_%S.%f")
    vid_name = t2_start + '.h264'
    print('the start time is ' + t2_start)
    camera.start_recording(vid_name)
    sleep(120)
    t1_end = datetime.now()
    t2_end = t1_end.strftime("%m-%d-%Y_%H_%M_%S.%f")
    print('the end time is ' + t2_end)
    camera.stop_recording()





#Need to convert with ffmpeg after. Yay.
#I did that once like this:
#ffmpeg -framerate 24 -i video.h264 -c copy output.mp4
