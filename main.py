# import cv2

# # Initialize video capture (camera)
# video_cap = cv2.VideoCapture(0)

# while True:
#     # Capture video frame by frame
#     ret, video_data = video_cap.read()
    
#     # Display the frame in a window named "Video"
#     cv2.imshow("Video", video_data)
    
#     # Exit when 'a' is pressed
#     if cv2.waitKey(10) == ord('a'):
#         break

# # Release the camera resource and close all windows
# video_cap.release()
# cv2.destroyAllWindows()  # To properly close the window
import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize video capture (camera)
video_cap = cv2.VideoCapture(0)

while True:
    # Capture video frame by frame
    ret, video_data = video_cap.read()
    
    # Convert the frame to grayscale (Haar Cascade works better on grayscale images)
    gray_frame = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Loop through all detected faces and draw rectangles around them
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the frame with rectangles around faces
    cv2.imshow("Face Detection", video_data)
    
    # Exit when 'a' is pressed
    if cv2.waitKey(10) == ord('a'):
        break

# Release the camera resource and close all windows
video_cap.release()
cv2.destroyAllWindows()
