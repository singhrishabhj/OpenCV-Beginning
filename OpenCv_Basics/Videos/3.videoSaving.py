import cv2

# Initialize video capture object using the default camera (index 0)
capture = cv2.VideoCapture(0)  # This line opens your computer's camera

# Define the codec and create a VideoWriter object to save the video
fourcc_code = cv2.VideoWriter_fourcc(*'XVID')  # Set the video codec to XVID
howToSave = cv2.VideoWriter('FileSaved.avi', fourcc_code, 20.0, (640, 480))  # Prepare to save a video file

# Check if the camera is opened successfully
if not capture.isOpened():
    print("Error: Could not open video device or file")
    exit()  # Exit the program if the camera is not accessible

# Loop to continuously capture and process frames
while True:
    # Read a frame from the camera
    ret, frame = capture.read()

    # Check if the frame was successfully captured
    if ret:
        # Write the frame to the output video file
        howToSave.write(frame)
        
        # Display the frame in a window named 'Frame'
        cv2.imshow('Frame', frame)

        # Check for user input; press 'q' to exit the loop
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    else:
        break  # Break the loop if no frame is received

# Release the video capture and video writer objects
capture.release()
howToSave.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
