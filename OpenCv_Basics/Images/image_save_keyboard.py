import cv2

'''
if somone press esc key, we want to detroy all the window without saving the file else if someone press 'S' key then we save this file as 1copyImage.png
'''
img = cv2.imread('1.png',-1)      #enable you to read the images
cv2.imshow('image',img)

k =cv2.waitKey(0) #this will close only when we close it or close the window

if k==27 : #if someone press esc key
    cv2.destroyAllWindows() #simple detroy all the window
elif k ==ord('s'):
     cv2.imwrite('newImageCopyKeySPressed.png',img)
     cv2.destroyAllWindows()