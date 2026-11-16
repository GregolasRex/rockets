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

#Uncomment below if you want to take a picture.
camera.start_preview()
sleep(2)
output_dir = '/home/pi/Desktop/photo_video/'

for i in range(10):
    datetime_for_name = datetime.now()
    photo_name = datetime_for_name.strftime("%m-%d-%Y:%H:%M:%S.%f") + '.jpg'
    #camera.capture('greg.jpg')
    camera.capture(output_dir + photo_name)
    print(photo_name + ' is saved')
    sleep(1)

'''
#This should take a video.
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(10)
camera.stop_recording()
'''

#Here is a basic loop to showcase the two video modes:
'''
framerates=[60,30]
resolution = [(1280,720), (1920,1080)]
output=['720.h264', '1080.h264']
for i in range(2):
    camera.resolution = resolution[i]
    camera.framerate = framerates[i]
    print('Now doing '+output[i])
    camera.start_recording(output[i])
    sleep(10)
    camera.stop_recording()
'''

#Need to convert with ffmpeg after. Yay.
#I did that once like this:
#ffmpeg -framerate 24 -i video.h264 -c copy output.mp4
