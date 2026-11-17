from picamera2 import Picamera2
import time

picam2 = Picamera2()
picam2.start_preview()

try:
    picam2.start()
    time.sleep(2)
    picam2.capture_file("sample_impage.jpg")
    print("wow")

finally:
    picam2.stop_preview()
    picam2.close()
