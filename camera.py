import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)

# Əl tanıma modulu
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

# Ekranın ölçülərini alırıq
screen_width, screen_height = pyautogui.size()

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Görüntünü güzgü effekti ilə çeviririk (sağ-sol qarışmasın)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            # Əl üzərindəki nöqtələri çəkirik
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark

            for id, landmark in enumerate(landmarks):
                # Şəhadət barmağının ucu (ID 8-dir)
                if id == 8:
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)

                    # Kameradakı koordinatları ekran koordinatlarına çeviririk
                    mouse_x = screen_width / frame_width * x
                    mouse_y = screen_height / frame_height * y

                    # Mousu hərəkət etdiririk
                    pyautogui.moveTo(mouse_x, mouse_y)

    cv2.imshow('Ellə Mouse Idarəsi', frame)

    # 'q' düyməsinə basanda proqram dayansın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.closeAllWindows()