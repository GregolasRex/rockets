from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
import time
from datetime import datetime
import sys

#Parameters
video_duration = int(sys.argv[1]) #seconds
video_prefix = datetime.now().strftime("%Y-%m-%d:%H:%M:%S")
#resolution = (4608, 2592)
resolution = (1920, 1080)
frame_rate = int(sys.argv[2])
res_config = {'size': resolution, 'format': 'YUV420'}
controls = {'FrameRate': frame_rate
		,'NoiseReductionMode': 3}

#Instantiate camera and set config
picam2 = Picamera2()
video_config = picam2.create_video_configuration( \
			main=res_config
			,controls=controls
			)
picam2.configure(video_config)
encoder = H264Encoder(framerate=frame_rate, enable_sps_framerate=True)

#for i in range(2):
#picam2.start_recording(encoder=encoder,output=f"{video_prefix}_{i:03}.h264")
picam2.start_recording(output="test.h264", encoder=encoder)
time.sleep(video_duration)
picam2.stop_recording()
