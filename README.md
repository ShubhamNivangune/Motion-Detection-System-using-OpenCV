# Motion-Detection-System-using-OpenCV

This motion detection system uses OpenCV to detect human presence and general motion in real-time using a webcam. It captures screenshots and plays an alarm sound when a person or motion is detected.

# Requirements
Python 3.x
OpenCV
haarcascade_fullbody.xml (pre-trained person detection model)
winsound library (for playing alarm sound on Windows)

# Installation
Clone the repository:
Copy code
git clone https://github.com/ShubhamNivangune/Motion-Detection-System-using-OpenCV.git
Install the required dependencies:
Copy code
pip install opencv-python
Download the pre-trained person detection model haarcascade_fullbody.xml and place it in the project directory.

(Optional) If you're using Windows, make sure you have the winsound library installed:

Copy code
pip install winsound

# Usage
Run the motion_detection.py script:
Copy code
python motion_detection.py
The webcam feed will be displayed in a window.

When a person or motion is detected, a screenshot will be captured and saved with a unique filename based on the current timestamp. An alarm sound will also be played to alert the user.

Press the 'q' key to exit the program.

# Customization
You can adjust the parameters for person detection and motion detection by modifying the scaleFactor, minNeighbors, and minSize arguments in the person_cascade.detectMultiScale() function and the cv2.threshold() function, respectively.

To change the alarm sound, replace the alarm.wav file in the project directory with your desired audio file. Make sure the new file is in WAV format.

# Acknowledgments
The person detection model used in this project is based on the Haar feature-based cascade classifiers. It was trained on a large dataset of full-body images and provides accurate person detection results.

The winsound library is used to play the alarm sound on Windows systems.

Feel free to copy and paste this README file into your project documentation.
