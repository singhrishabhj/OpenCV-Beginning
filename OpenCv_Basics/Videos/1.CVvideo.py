import cv2

capture = cv2.VideoCapture(0) #initialize video capturing object



#this capture live stream from camera and also used to display the video file too

# You can the video file as an arguments or you want provide your device index of your camera 0,-1->default camera , 1- second camera , 2- second camera

if not capture.isOpened():
    print("Error: Could not open video device or file")
    exit() #Check if the camera/video capturing object is opened successfully

# Now we will create a while which order to capture the frame continously

while(True): 

    ret, frame = capture.read() #while this is true we want to capture the frame
     
    if not ret:
        print("Error :Failed to capture frame") #using it to test it the frame is not returning true or there is error orCheck if the frame is valid

    # if this read method will return true or false ,if it is true,the frame is available and then it will saved into the frame varibale

    '''
        capture.read(): This method reads the next frame from the video capture object (cap).

    Upon calling cap.read(), it returns two values:
        1.ret: A boolean value (True or False) indicating if a frame was successfully read. If the frame is read correctly, ret is True; otherwise, it's False.
        2.frame: The actual image data of the frame captured. This is represented as a NumPy array.
    '''

    cv2.imshow('Frame',frame) 
    #Display the Frame
    
    #used to show the video (the frame will be showed which is stored in the frame variable)
    
    key=cv2.waitKey(1) & 0xFF #Wait for a keypress 

    if key==ord('q'):  #Exit the loop if 'q'is pressed
        break

capture.release()
cv2.destroyAllWindows()



