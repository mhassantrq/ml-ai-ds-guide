#   import the cv2 library for image processing
import cv2


#   to load or read an image. the 'imread()' function from the cv2 library is used.
img = cv2.imread('img_cal.png', 1)

"""
the first path of image is passed to the imread.

the second parameter currently having value of 1 represents the color if image reading.

if you want to read an image as colored format, 1 is written.
if you want to read an image as black and white format, 0 is written.
"""


#   lets print the values of image as array of numpy
print(img)