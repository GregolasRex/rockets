#!/bin/bash

#echo "video $1 converting"
MP4Box -add /home/pi/Desktop/$1.h264 /home/pi/Desktop/$1.mp4
echo "video conversion complete"
