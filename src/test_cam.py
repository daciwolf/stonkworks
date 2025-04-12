# save as test_camera.py
import cv2

cap = cv2.VideoCapture(1, cv2.CAP_V4L2)
if not cap.isOpened():
    print("Camera not found")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("PiCam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
