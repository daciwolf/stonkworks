import cv2
from picamera2 import Picamera2
import time

# Initialize camera
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'BGR888'}))

# Start camera
picam2.start()
time.sleep(2)  # Let it warm up

# Stream loop
while True:
    frame_bgr = picam2.capture_array()
    frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)  # Fix colors

    cv2.imshow("Camera Preview (RGB Fixed)", frame_rgb)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
