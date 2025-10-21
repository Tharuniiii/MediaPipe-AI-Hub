import cv2
import mediapipe as mp
import numpy as np
import streamlit as st

def run():
    st.title("🎨 Air Canvas – Draw with Your Hand")
    st.markdown("Move your index finger in the air to draw. Press 'c' to clear.")

    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    stframe = st.empty()

    canvas = None
    prev_x, prev_y = 0, 0

    with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break

            frame = cv2.flip(frame, 1)
            if canvas is None:
                canvas = np.zeros_like(frame)

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    index_finger = hand_landmarks.landmark[8]
                    h, w, _ = frame.shape
                    x, y = int(index_finger.x * w), int(index_finger.y * h)

                    if prev_x == 0 and prev_y == 0:
                        prev_x, prev_y = x, y

                    cv2.line(canvas, (prev_x, prev_y), (x, y), (255, 0, 0), 5)
                    prev_x, prev_y = x, y

            # Combine drawing and frame
            frame = cv2.addWeighted(frame, 0.6, canvas, 0.4, 0)

            stframe.image(frame, channels="BGR", use_column_width=True)

    cap.release()
