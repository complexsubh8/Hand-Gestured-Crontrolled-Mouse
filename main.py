import cv2
import mediapipe as mp
import pyautogui as pt
import time

# Initialize camera and hand tracking
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pt.size()

# Cursor smoothing
smoothening = 5
prev_x, prev_y = 0, 0

# Tap detection variables
prev_index_y = 0
tap_time = 0
tap_threshold = 40  # Minimum movement for a tap
cooldown = 0.5  # Prevents multiple rapid taps

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
            landmarks = hand.landmark

            index_x, index_y = 0, 0
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id == 8:  # Index finger tip
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y
                    cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)  # Green circle on index tip

            # Cursor movement with smooth transition
            curr_x = prev_x + (index_x - prev_x) / smoothening
            curr_y = prev_y + (index_y - prev_y) / smoothening
            pt.moveTo(curr_x, curr_y)
            prev_x, prev_y = curr_x, curr_y

            # Tap detection
            current_time = time.time()
            if prev_index_y - index_y > tap_threshold:  # Detect downward movement
                if (current_time - tap_time) > cooldown:  # Prevent multiple taps
                    pt.click()
                    tap_time = current_time

            prev_index_y = index_y  # Update last known position of the index finger

    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
