gst-launch-1.0 libcamerasrc ! \
	video/x-raw,width=640,height=480,framerate=30/1 ! \
	v4l2h264enc extra-controls="controls,h264_profile=0,video_bitrate=1200000" ! \
	'video/x-h264,level=(string)4' ! \
	mpegtsmux ! \
	udpsink host=10.110.15.1 port=5000 sync=false
