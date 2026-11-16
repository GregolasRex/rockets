from time import sleep
from picamera import PiCamera

#This is the initial step.
camera = PiCamera()

#For resolution and frame rate, there are trade-offs.

#If you want higher resolution, go down to 30 fps:
camera.resolution = (1920, 1080)
camera.framerate = 30


camera.resolution = (1920,1080)
camera.framerate = 30
print('Now doing '+'1080.h264')
camera.start_recording('1080.h264')
elapsed = 0
for i in range(120):
    sleep(60)
    elapsed += 60
    print('minutes elapsed = ' + str(elapsed%60))
camera.stop_recording()





#Need to convert with ffmpeg after. Yay.
#I did that once like this:
#ffmpeg -framerate 24 -i video.h264 -c copy output.mp4
