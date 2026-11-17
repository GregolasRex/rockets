from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder, Quality
import time
from datetime import datetime
import sys

#Parameters
video_duration = int(sys.argv[1]) #seconds
frame_rate = int(sys.argv[2]) #frames per second
video_prefix = datetime.now().strftime("%Y-%m-%d:%H:%M:%S")
storage_dir = "/home/pi/Desktop/photo_video/"
#resolution = (4608, 2592)
resolution = (1920, 1080)
#resolution = (1280, 720)
res_config = {'size': resolution, 'format': 'YUV420'} #YUV420 #XBGR8888
controls = {'FrameRate': frame_rate
		,'NoiseReductionMode': 3}

#Create and configure a camera object to take test photos
still_cam = Picamera2()
still_config = still_cam.create_still_configuration( \
				main={'size': resolution}
				)
still_cam.configure(still_config)
still_cam.start()
time.sleep(2) #Let the lil baby camera fully set up

#test photos
for i in range(10):
	still_cam.capture_file(f"{storage_dir}{i:02}.jpg")
	time.sleep(1)

still_cam.stop()

#get rid of the test cam just cuz
#del still_cam


#Instantiate camera and set video config
picam2 = Picamera2()
video_config = picam2.create_video_configuration( \
			main=res_config
			,controls=controls
			)
picam2.configure(video_config)
encoder = H264Encoder(framerate=frame_rate, enable_sps_framerate=True)

for i in range(1000):
	file_nm = f"{storage_dir}{video_prefix}_{i:03}.h264"
	picam2.start_recording(encoder=encoder
				,output=file_nm
				,quality=Quality.VERY_HIGH #VERY_HIGH
				,pts=f"{storage_dir}{video_prefix}_{i:03}.txt")
	time.sleep(video_duration)
	picam2.stop_recording()
