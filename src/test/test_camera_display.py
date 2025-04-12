import cv2
from picamera2 import Picamera2
import time

# Initialize camera
picam2 = Picamera2()

# Configure camera for preview with color format
picam2.configure(picam2.create_preview_configuration(main={"format": 'BGR888'}))

# Start the camera
picam2.start()

# Enable auto controls
picam2.set_controls({
    "AfMode": 1,        # Continuous autofocus (1 = auto)
    "AeEnable": True,   # Auto exposure
    "AwbEnable": True,  # Auto white balance
    # Optional tuning (you can comment these out to use defaults)
    "Brightness": 0.0,      # Range: -1.0 to 1.0
    "Contrast": 1.0,        # Range: 0.0 to 32.0
    "Saturation": 1.0       # Range: 0.0 to 32.0
})

time.sleep(2)  # Let autofocus, AWB, and AE settle

# Stream loop
while True:
    frame_bgr = picam2.capture_array()
    frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)

    cv2.imshow("Camera Preview (Auto Focus & Color)", frame_rgb)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
