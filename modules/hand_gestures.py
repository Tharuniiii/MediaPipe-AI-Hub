import cv2
import mediapipe as mp
import streamlit as st
import tempfile
import os

def run():
    st.title("✋ Hand Gesture Recognition")

    st.markdown("""
    Detect and visualize hand gestures in real-time using **MediaPipe Hands**.
    You can use your **webcam** or **upload a video**.
    """)

    input_source = st.radio("🎥 Select Input Source", ("Webcam", "Upload Video"))

    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    stframe = st.empty()

    if input_source == "Upload Video":
        uploaded_file = st.file_uploader("📁 Upload your video file", type=["mp4", "mov", "avi"])
        if uploaded_file:
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            temp_file.write(uploaded_file.read())
            video_path = temp_file.name
            cap = cv2.VideoCapture(video_path)
        else:
            st.warning("Please upload a video to start.")
            return
    else:
        cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )

        st.image("example.jpg", width="auto")

        if input_source == "Upload Video":
            cv2.waitKey(1)

    cap.release()
    if input_source == "Upload Video":
        os.remove(temp_file.name)
    st.success("✅ Processing completed.")
