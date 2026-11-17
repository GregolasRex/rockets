import subprocess
from subprocess import call
import glob

video_dir = "/home/pi/Desktop/photo_video/"
script_dir = "/home/pi/Desktop/scripts/"
old_type = ".h264"
new_type = ".mp4"

fileglob = glob.glob(video_dir + "*" + old_type)
#print(fileglob)

for file in fileglob:
    new_file = file.replace(old_type, "").replace(video_dir, "")
#    new_file = new_file.replace(video_dir, "")
    print("new file: " + new_file)
    print("starting file conversion: " + file)
#    rc = call(script_dir + "convert_all_vids.sh" + " " + new_file)
#    rc = call(script_dir + "convert_all_vids.sh")
    subprocess.check_call(script_dir + "convert_all_vids.sh %s" % new_file, shell=True)
    print("file conversion finished: " + new_file)

#rc = call(/home/pi/Desktop/photo_video/convert_all_vids.sh
