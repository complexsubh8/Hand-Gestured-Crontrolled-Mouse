# 🖐️ Hand Gesture Controlled Mouse (Python)

Control your mouse using **hand gestures** through a webcam using computer vision techniques.

---

## ✨ Features

- Mouse cursor movement using hand motion
- Left and right click using finger gestures
- Real-time hand tracking
- No external hardware required
- Lightweight and easy to use

---

## 🧰 Tech Stack

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

---


---

## ⚙️ Installation

pip install opencv-python mediapipe pyautogui numpy

---

## ▶️ Run the Project


Make sure your webcam is enabled and lighting is sufficient.

---

## ✋ Gesture Mapping

| Gesture | Action |
|--------|--------|
| Index finger up | Move cursor |
| Thumb + Index close | Left click |
| Index + Middle close | Right click |
| Palm open | Pause movement |

---

## 🧠 Working Principle

- Capture webcam frames
- Detect hand landmarks using MediaPipe
- Track fingertip coordinates
- Map hand movement to screen resolution
- Perform mouse actions using PyAutoGUI

---

## 🚧 Limitations

- Sensitive to lighting conditions
- Minor latency on low-end systems
- Accuracy depends on webcam quality

---

## 🔮 Future Improvements

- Scroll control
- Gesture customization
- Multi-hand support
- Improved smoothing and accuracy

---

## 👤 Author

Subham

---

## 📜 License

MIT License
