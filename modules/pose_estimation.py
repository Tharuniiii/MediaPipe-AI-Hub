import cv2
import mediapipe as mp
import streamlit as st

def run():
    st.title("🧍 Pose Estimation")
    st.markdown("Tracks human pose keypoints like shoulders, elbows, knees, etc.")

    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    stframe = st.empty()

    with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as pose:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(rgb)

            if results.pose_landmarks:
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            stframe.image(frame, channels="BGR", use_column_width=True)

    cap.release()
