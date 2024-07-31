import cv2
img = cv2.imread('image.png',1)

#we are going to oiverrirde this image
# we are going to draw line on the image
img = cv2.line(img,(0,0),(255,255), (0, 0, 255) , 5)

'''
The arguments decription taken by the .line function: 
- `img`: The image where the line will be drawn.
- `cv2.line`: OpenCV function to draw a line.
- `(0,0)`: Start point of the line (top-left corner).
- `(255,255)`: End point of the line.
- `(0, 0, 255)`: Line color (red in BGR format).
- '5' : This give thickness
'''
#for arrowed line

img = cv2.arrowedLine(img,(0,255),(255,255), (78, 0, 255) , 5) 
#this will overlap the previous line and the arrow line only show if cordinate are same
 
# for rectangle

img= cv2.rectangle(img,(384,0),(510,128), (78, 48, 255) , 5)
# if we enter -1 rather than giving the thickness to the rectangle it will fill the rectangle
'''
cv2.recctangle function draw a rectangle :
(x1,y1) (x2,y2)
(384,0) (510,128)
x1,y1---------
|             |
|             |
|             |
----------x2,y2
'''

img= cv2.rectangle(img,(680,0),(730,168), (78, 48, 29) , -1)
#this will fill the rectangle
#mainly -1 will fill the color

#for circle

img= cv2.circle(img,(663,890),20,(78, 48, 295) , 3) 


img= cv2.circle(img,(489,880),30, (78, 68, 255) , -1) #filled circle


#input text
font=cv2.FONT_HERSHEY_DUPLEX

img= cv2.putText(img,"Haanji!",(190,500),font,5,(234,78,32),3,cv2.LINE_AA)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()