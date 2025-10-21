import streamlit as st
from modules import face_mesh, hand_tracking, pose_estimation, holistic, object_detection, hand_gestures, air_canvas

st.set_page_config(page_title="MediaPipe AI Hub", layout="wide")

st.sidebar.title("🧠 MediaPipe AI Hub")
option = st.sidebar.selectbox(
    "Select a Module",
    (
        "Face Mesh",
        "Hand Tracking",
        "Pose Estimation",
        "Holistic Detection",
        "Object Detection",
        "Hand Gestures",
        "Air Canvas"
    )
)

if option == "Face Mesh":
    face_mesh.run()
elif option == "Hand Tracking":
    hand_tracking.run()
elif option == "Pose Estimation":
    pose_estimation.run()
elif option == "Holistic Detection":
    holistic.run()
elif option == "Object Detection":
    object_detection.run()
elif option == "Hand Gestures":
    hand_gestures.run()
elif option == "Air Canvas":
    air_canvas.run()
