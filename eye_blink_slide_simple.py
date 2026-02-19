import cv2
import pyautogui
import time
import os

# Get current folder path
current_dir = os.path.dirname(os.path.abspath(__file__))

# Haar cascade for eye detection (relative path)
eye_cascade_path = os.path.join(current_dir, "haarcascade_eye.xml")
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

# Check if cascade loaded correctly
if eye_cascade.empty():
    print("Error: haarcascade_eye.xml not found!")
    exit()

# Start webcam
cap = cv2.VideoCapture(0)

closed_frames = 0
blink_count = 0
last_blink_time = 0
cooldown = 1.0  # 1 second cooldown between blinks

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

    # Simple logic: if no eyes detected -> eyes closed
    if len(eyes) == 0:
        closed_frames += 1
    else:
        if closed_frames > 2:
            blink_count += 1
            last_blink_time = time.time()
        closed_frames = 0

    # Handle blink actions with cooldown
    current_time = time.time()
    if blink_count > 0 and current_time - last_blink_time > cooldown:

        if blink_count == 1:
            print("Slide UP")
            pyautogui.press("up")   # Slide UP

        elif blink_count == 2:
            print("Slide DOWN")
            pyautogui.press("down")  # Slide DOWN

        blink_count = 0

    cv2.imshow("Eye Blink Slide Control (Simple)", frame)

    if cv2.waitKey(1) == 27:  # ESC key to exit
        break

cap.release()
cv2.destroyAllWindows()
