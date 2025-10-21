import cv2
import mediapipe as mp
import streamlit as st
import tempfile

def run():
    st.title("✋ Hand Tracking")
    st.markdown("Tracks hand movements in real-time or uploaded videos.")

    option = st.radio("Select Input Source", ["Webcam", "Upload Video"])

    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils

    if option == "Upload Video":
        video_file = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])
        if video_file is not None:
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(video_file.read())
            cap = cv2.VideoCapture(tfile.name)
        else:
            st.warning("Please upload a video file.")
            return
    else:
        cap = cv2.VideoCapture(0)

    stframe = st.empty()

    with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7) as hands:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            stframe.image(frame, channels="BGR", use_column_width=True)

    cap.release()
