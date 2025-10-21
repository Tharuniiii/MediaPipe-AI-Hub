# MediaPipe-AI-Hub
MediaPipe AI Hub is a Streamlit-based web application that brings together multiple real-time AI vision modules powered by Google MediaPipe and OpenCV.

An interactive Streamlit application that combines multiple **MediaPipe** computer vision modules — including **Face Mesh**, **Hand Tracking**, **Pose Estimation**, **Holistic Detection**, **Hand Gestures**, and **Air Canvas** — into one unified platform.  

This project demonstrates how MediaPipe’s pre-built solutions can be integrated with **OpenCV** and **Streamlit** to perform real-time detection and visualization using your webcam.

---

## 📸 Features  
```
| Module | Description |
|:-------|:-------------|
| 👁️ **Face Mesh** | Detects and maps 468 facial landmarks on the user’s face in real time. |
| ✋ **Hand Tracking** | Tracks both hands, detecting 21 landmarks per hand. |
| 🧍 **Pose Estimation** | Estimates human body posture and key skeletal points. |
| 🧘 **Holistic Detection** | Combines face, hand, and pose models for full-body landmark tracking. |
| 🤟 **Hand Gestures** | Recognizes and interprets predefined hand gestures. |
| 🎨 **Air Canvas** | Lets users draw in the air using their index finger as a brush. |
```

---

## 🗂️ Project Structure  
```
mediapipe_ai_hub/
│
├── modules/
│ ├── face_mesh.py
│ ├── hand_tracking.py
│ ├── pose_estimation.py
│ ├── holistic.py
│ ├── hand_gestures.py
│ ├── air_canvas.py
│
├── app.py # Main Streamlit app (contains sidebar and routing)
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```


---

## ⚙️ Installation  
1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/mediapipe_ai_hub.git
cd mediapipe_ai_hub
```

2️⃣ Create and activate a virtual environment
```
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3️⃣ Install required packages
```
pip install -r requirements.txt
streamlit run app.py
```

# 🧠 How It Works

Each module (for example, face_mesh.py or pose_estimation.py) defines a run() function that:

Initializes the corresponding MediaPipe solution.

Captures frames from your webcam using OpenCV.

Processes the frames through the model to detect landmarks.

Displays the processed frames in real-time through Streamlit.

# 💻 Tech Stack

Language: Python 3.8+

Libraries:

Streamlit
 – Interactive web app framework

MediaPipe
 – Real-time ML vision framework

OpenCV
 – Image and video processing

NumPy
 – Numerical computations

 # 🧩 System Requirements
 ```bash
| Component | Requirement                                |
| :-------- | :----------------------------------------- |
| OS        | Windows / macOS / Linux                    |
| Python    | 3.8 – 3.12                                 |
| RAM       | ≥ 4 GB                                     |
| Webcam    | Required for live modules                  |
| GPU       | Optional (CPU is sufficient for MediaPipe) |
```

# 🌟 Future Enhancements

Add support for uploading images and videos.

Implement gesture-based control for app navigation.

Introduce multi-threaded webcam handling for better FPS.

Add saving/exporting options for Air Canvas drawings.

👨‍💻 Author

Tharuni T
Undergraduate Student | AI & Computer Vision Enthusiast

---
"Empowering creativity through computer vision and AI." ✨
