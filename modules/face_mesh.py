import cv2
import mediapipe as mp
import streamlit as st

def run():
    st.title("👁️ Face Mesh Detection")
    st.markdown("Detects 468 facial landmarks using Mediapipe FaceMesh model.")

    mp_face_mesh = mp.solutions.face_mesh
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    stframe = st.empty()

    with mp_face_mesh.FaceMesh(
        max_num_faces=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as face_mesh:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(rgb)

            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    mp_drawing.draw_landmarks(
                        frame,
                        face_landmarks,
                        mp_face_mesh.FACEMESH_CONTOURS,
                        mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                        mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=1)
                    )

            stframe.image(frame, channels="BGR", use_column_width=True)

    cap.release()
