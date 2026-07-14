# Virtual Mouse using Hand Gestures

Control your computer mouse using only your hand and a webcam.

This project uses **OpenCV**, **MediaPipe Hands**, and **PyAutoGUI** to detect hand landmarks in real time and convert finger movements into mouse actions.

---

## Features

- 🖱️ Move mouse cursor using your index finger
- 👆 Left click using thumb and index finger gesture
- 👆👆 Double click using a closer finger gesture
- 👉 Right click using the middle finger gesture
- 📷 Real-time webcam tracking
- ⚡ FPS display

---

## Technologies Used

- Python
- OpenCV
- MediaPipe
- PyAutoGUI

---

## Requirements

Install the required packages.

```bash
pip install opencv-python mediapipe pyautogui
```

---

## How to Run

Clone the repository

```bash
git clone https://github.com/yourusername/Virtual-Mouse.git
```

Move into the project folder

```bash
cd Virtual-Mouse
```

Run the program

```bash
python virtual_mouse.py
```

Allow webcam access when prompted.

---

## Hand Gestures

| Gesture | Action |
|----------|--------|
| Move Index Finger | Move Mouse Cursor |
| Thumb + Index Finger Close | Left Click |
| Thumb + Index Finger Very Close | Double Click |
| Middle Finger Gesture | Right Click |

---

## Project Structure

```
Virtual-Mouse/
│
├── virtual_mouse.py
├── README.md
├── screenshots/
│   ├── gesture.png
│   └── working.png
└── demo.mp4
```

---

## Future Improvements

- Cursor smoothing
- Scroll gesture
- Drag and drop gesture
- Volume control
- Brightness control
- Multi-monitor support
- Gesture customization
- Better click detection using Euclidean distance
- GUI for settings

---

## Concepts Used

- Computer Vision
- Hand Landmark Detection
- Human Computer Interaction (HCI)
- Gesture Recognition
- Real-Time Video Processing

---

## Author

Aviraj Ahlawat
