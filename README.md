# Hand Tracking Volume Controller
This Python project, "Hand Gesture Controlled Volume," allows you to control the system's audio volume by using hand gestures. It utilizes computer vision techniques with OpenCV and the MediaPipe library to detect and track hand movements in real-time, converting specific gestures into volume level adjustments.

● Project Components

1 ● HandTrackingVolumeControl.py

The main script, HandTrackingVolumeControl.py, is responsible for detecting and tracking hand gestures to control the audio volume. It uses the following key components:

OpenCV (cv2): Captures video from your computer's camera and displays the video feed. It also provides image processing capabilities for drawing on the video.

pycaw: Interacts with the Windows Core Audio API to control the system's audio volume.

HandTrackingModule.py: A custom module that uses MediaPipe to detect and track hand landmarks and gestures.

In the main loop of the script, it continuously detects the position of your hand's thumb and index finger, calculates the distance between them, and adjusts the system's audio volume based on your hand's proximity. The script also displays a graphical representation of the volume level on the screen.

2 ● HandTrackingModule.py

This module, HandTrackingModule.py, encapsulates the hand detection and tracking functionality using MediaPipe. It includes:

HandsDetector class: Initializes the hand detection model, configures its parameters, and provides methods to detect and track hands in images or video frames.
The module is reusable and can be applied to other projects involving hand tracking.

● How to Use

1 ● Make sure you have Python and the required libraries (OpenCV, pycaw, and MediaPipe) installed.

2 ● Run HandTrackingVolumeControl.py.

3 ● A live video feed from your camera will appear. Use your hand gestures to control the volume level.

4 ● The script will continuously adjust the system's audio volume based on the distance between your thumb and index finger. The volume level will be displayed on the screen as a percentage.

● Note

This project is designed to work on Windows due to its reliance on the Windows Core Audio API (pycaw).

Make sure your camera is functional and accessible by OpenCV.

Please refer to the project's dependencies and installation instructions to ensure a smooth setup.
