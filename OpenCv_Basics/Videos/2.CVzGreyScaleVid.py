import cv2

# Initialize video capturing object (replace with the correct device index or video file path)
capture = cv2.VideoCapture(0)  # Example: 0 for default camera

# Check if the camera/video capturing object is opened successfully
if not capture.isOpened():
    print("Error: Could not open video device or file")
    exit()

# Loop to capture and display frames continuously
while True:
    ret, frames = capture.read()  # Read a frame from the video capture

    # Check if the frame is valid
    if not ret:
        print("Error: Failed to capture frame")
        break

    grayScaleCvt =cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY) #this cvtColor function convert Grayscale
   
   
    # Display the frame in a window named 'Frame'
    cv2.imshow('Frame', grayScaleCvt )

    # Wait for a key press; check if 'q' is pressed to exit
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
capture.release()
cv2.destroyAllWindows()
