import cv2
import numpy as np
import streamlit as st

def run():
    st.title("🚗 Vehicle / Object Detection")
    st.markdown("Detects moving objects (like vehicles or people) using background subtraction.")

    video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

    if video_file is not None:
        tfile = open("temp_video.mp4", "wb")
        tfile.write(video_file.read())
        cap = cv2.VideoCapture("temp_video.mp4")

        fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50)
        stframe = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.resize(frame, (800, 600))
            mask = fgbg.apply(frame)

            _, mask = cv2.threshold(mask, 250, 255, cv2.THRESH_BINARY)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))

            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            count = 0

            for cnt in contours:
                if cv2.contourArea(cnt) > 800:
                    x, y, w, h = cv2.boundingRect(cnt)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
                    count += 1

            cv2.putText(frame, f"Objects Detected: {count}", (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

            stframe.image(frame, channels="BGR", use_column_width=True)

        cap.release()
    