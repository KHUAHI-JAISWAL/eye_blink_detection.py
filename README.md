# Eye Blink Based Slide Control System

This project uses computer vision to detect eye blinks in real time and
allows controlling slides (scroll up and down) using eye movements and blinks.

## Objective
To build a hands-free slide control system using eye blink detection.

## Problem Type
Computer Vision / Human–Computer Interaction

## Description
The system captures live video from a webcam, detects the eyes using a Haar
Cascade classifier and identifies blink events. Based on the detected blink
pattern, the slides are scrolled up or down automatically.

This project is useful for hands-free presentations and accessibility support.

## Tools & Libraries
- Python
- OpenCV
- PyAutoGUI
- Haar Cascade Classifier

## Files
- eye-blink-detection.ipynb   (main notebook)
- haarcascade_eye.xml        (eye detection file)

## Features
- Real-time eye detection using webcam
- Eye blink detection
- Slide / screen scrolling control (up and down)
- Hands-free slide navigation

## How to run
1. Open the notebook file.
2. Make sure the file `haarcascade_eye.xml` is in the same folder.
3. Run all cells in order.
4. Allow camera access.
5. Open your presentation and control slide scrolling using eye blinks.

## Author
Khushi Jaiswal
