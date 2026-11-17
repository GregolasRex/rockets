import subprocess
import sys
import os

#input_ts = sys.argv[1]+'.txt'
#input_vid = sys.argv[1]+'.h264'
path = "/home/pi/Desktop/photo_video/"

for filename in os.listdir(path):
	if filename.endswith(".h264"):
		# Create the output mp4 video
		# Add a line at the top of the timestamp file to
		# facilitate correct timestamp interpretation
		base_name = os.path.splitext(os.path.basename(filename))[0]
		target_file = os.path.join(path, f"{base_name}.mkv")
		source_file = os.path.join(path, f"{base_name}.h264")
		print(base_name)
		print(target_file)
		merge = subprocess.Popen([
    				"mkvmerge", "-o", target_file,
				 "--timestamps", f"0:{path}{base_name}.txt",
   				source_file
				])
		merge.wait()
