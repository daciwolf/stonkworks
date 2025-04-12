from picamera2 import Picamera2
import numpy as np
import time
from PIL import Image  # Import Pillow for saving images

# Initialize the camera
picam2 = Picamera2()

# Configure the camera to capture still images
picam2.configure(picam2.create_still_configuration())

# Start the camera preview (optional)
picam2.start()

# Let the camera warm up
time.sleep(2)

# Capture an image as a NumPy array
image = picam2.capture_array()

# Now you can use the `image` NumPy array with OpenCV or other libraries
print(f"Captured image shape: {image.shape}")

# Convert the NumPy array to a PIL Image and save it
im = Image.fromarray(image)  # Convert the NumPy array to a PIL Image
im.save("captured_image.jpg")  # Save the image as a .jpg file

print("Image saved as captured_image.jpg")
