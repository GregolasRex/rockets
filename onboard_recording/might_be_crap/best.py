from picamera2 import Picamera2, Preview
import time
import sys

# get frame width, height from command line args
w = int(sys.argv[1])
h = int(sys.argv[2])
res = (w, h)
fps = int(sys.argv[3])

picam2 = Picamera2()

# use video config (optimized for speed) other format XBGR8888
res_config = picam2.create_video_configuration( \
	main = {"size": res, "format": "YUV420"} \
)
controls = {"FrameRate": fps, "NoiseReductionMode": 3}

#video_config = picam2.create_video_configuration( \
#			main = res_config \
#			,controls = controls \
#		)
#picam2.configure(video_config)

#hardware-accelerated preview
picam2.start_preview(Preview.QTGL)

picam2.start()

try:
	while True:
		time.sleep(1) #preview runs independently
except KeyboardInterrupt:
	pass
finally:
	picam2.stop()

