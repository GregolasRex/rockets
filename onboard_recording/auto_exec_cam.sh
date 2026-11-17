#!/bin/sh

export MAIN_PATH=/home/pi/Desktop
export PROGRAM_PATH=$MAIN_PATH/programs
export LOG_PATH=$MAIN_PATH/logs

export TIMESTAMP=`date +%Y-%m-%d_%H_%M_%S`
echo "timestamp " $TIMESTAMP
export LOG_NAME=log_$TIMESTAMP.txt

echo "starting program" >> $LOG_PATH/$LOG_NAME

python $PROGRAM_PATH/ten_photos_ts_nm.py

