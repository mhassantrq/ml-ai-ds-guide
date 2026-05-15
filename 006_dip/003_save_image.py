import cv2

img = cv2.imread('img_cal.png', 1)

"""
the function used to save an image is the 'imwrite' from cv2
the first parameter is the new image path and name with extension
the second parameteer is the image itself
"""
cv2.imwrite('newimage.jpg', img)