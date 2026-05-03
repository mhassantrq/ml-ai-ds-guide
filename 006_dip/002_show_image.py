import cv2

img = cv2.imread('img_cal.png', 1)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()