#!/bin/bash

#echo "video $1 converting"
MP4Box -add /home/pi/Desktop/photo_video/$1.h264 /home/pi/Desktop/photo_video/$1.mp4
echo "video conversion complete"
