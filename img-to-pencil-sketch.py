''' image to pencil art 
by Mr_Mystery check out our yt channel link in readme file
'''

import cv2        #importing opencv2 
img = cv2.imread('image.jpg')     # reading the image       you can give the path of your image file here insted of image.jpg

#converting the image to pencil sketch
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
inverted_image = 255 - gray_image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 5)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

#showing the result
cv2.imshow("original image", img)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)

