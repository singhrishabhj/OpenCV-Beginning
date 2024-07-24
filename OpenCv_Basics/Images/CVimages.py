'''
Getting started with imagse
->Reading an Images
->Check image attribute like datatype and shape
->Matrix reprsentation of an image in Numpy
->Color Images and splitting/merging images channels
->Displaying images using matplotlib
->VSaving Images
'''

#read and write images for your projects

import cv2

img = cv2.imread('1.png',0)      #enable you to read the images

print(img)
'''
give you the matrix , it read all the pixel from images and assigned it to img variable 

// output 
[[153 147 159 ...  56  34  34]
 [146 131 103 ...  93  50  53]
 [134 114  93 ...  61  46  53]
 ...
 [ 85  72  87 ...  84  78 101]
 [ 85  76  98 ...  85  78  72]
 [ 80  78 103 ...  87  70  59]]
'''

cv2.imshow('image',img)

cv2.waitKey(5000) #image show only for 5 sec 
cv2.destroyAllWindows() 

cv2.imwrite('1CopyImage.png',img) #used to write image int he form of file
