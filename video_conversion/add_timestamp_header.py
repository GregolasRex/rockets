import os
import sys

def add_row_to_top(path, row_content):
	for f in os.listdir(path):
		if f.endswith(".txt"):
			#Target file to which row will be added
			f_path = os.path.join(path, f)

			with open(f_path, "r") as file_test:
				if file_test.readline() != row_content:
					#Read the file content
					with open(f_path, "r") as file:
						content = file.readlines()
					#Add the new row at the top
					content.insert(0, new_row)
					#Write the content back to the file
					with open(f_path, "w") as file:
						file.writelines(content)

#p = sys.argv[1]
p = "/home/pi/Desktop/photo_video/"
new_row = "# timestamp format v2\n"

add_row_to_top(path = p, row_content = new_row)
