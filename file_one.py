import cv2
import winsound
import datetime

# Load the pre-trained person detection model
person_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Open the camera
video = cv2.VideoCapture(0)  # 0 represents the default camera

# Initialize variables for motion detection
previous_frame = None
motion_detected = False

# Loop through the camera frames
while True:
    # Read a frame from the camera
    ret, frame = video.read()

    # Convert the frame to grayscale for motion detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # If this is the first frame, save it for later comparison
    if previous_frame is None:
        previous_frame = gray
        continue

    # Compute the absolute difference between the current frame and the previous frame
    frame_delta = cv2.absdiff(previous_frame, gray)

    # Apply a threshold to the frame delta
    threshold = cv2.threshold(frame_delta, 30, 255, cv2.THRESH_BINARY)[1]

    # Perform person detection on the current frame
    persons = person_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # If a person is detected or motion is detected, capture a screenshot and play an alarm
    if len(persons) > 0 or cv2.countNonZero(threshold) > 0:
        motion_detected = True

        # Generate a unique filename using the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"screenshot_{timestamp}.jpg"
        # Capture a screenshot
        cv2.imwrite(filename, frame)

        # Play an alarm sound (Windows-only)
        winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)

    # Display the camera frame
    cv2.imshow('Camera Feed', frame)

    # Update the previous frame for the next iteration
    previous_frame = gray

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the windows
video.release()
cv2.destroyAllWindows()
