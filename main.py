import cv2

# Initialize video capture (camera)
video_cap = cv2.VideoCapture(0)

while True:
    # Capture video frame by frame
    ret, video_data = video_cap.read()
    
    # Display the frame in a window named "Video"
    cv2.imshow("Video", video_data)
    
    # Exit when 'a' is pressed
    if cv2.waitKey(10) == ord('a'):
        break

# Release the camera resource and close all windows
video_cap.release()
cv2.destroyAllWindows()  # To properly close the window
