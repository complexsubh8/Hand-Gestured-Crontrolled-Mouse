🖐️ Hand Gesture Controlled Mouse using Python

A computer vision–based virtual mouse that allows users to control mouse movement and clicks using hand gestures, eliminating the need for physical input devices. This project uses a webcam to track hand landmarks in real time and map them to mouse actions.

🚀 Features

🖱️ Control mouse cursor using hand movement

👆 Left click using finger gesture

✌️ Right click using finger gesture (optional)

🔍 Real-time hand tracking

📷 Webcam-based input

💻 Works on Windows / Linux / macOS

🛠️ Technologies Used

Python

OpenCV – for video capture and image processing

MediaPipe – for hand landmark detection

PyAutoGUI – for controlling mouse actions

NumPy – for calculations and array operations

📁 Project Structure
hand-gesture-mouse/
│
├── main.py                # Main program
├── requirements.txt       # Required libraries
├── README.md              # Project documentation
└── assets/                # Demo images / videos (optional)

⚙️ Installation

Clone the repository

git clone https://github.com/your-username/hand-gesture-mouse.git
cd hand-gesture-mouse


Install dependencies

pip install -r requirements.txt


If requirements.txt is not present:

pip install opencv-python mediapipe pyautogui numpy

▶️ How to Run
python main.py


Make sure:

Your webcam is connected

You have proper lighting for better hand detection

✋ Gesture Controls (Example)
Gesture	Action
Index finger up	Move mouse
Index + Thumb close	Left click
Index + Middle close	Right click
Palm open	Pause control

(Gestures may vary based on implementation)
