import cv2

img = cv2.imread('img_cal.png', 1)

"""
Outputs height, weight and channels in this order
"""
print(f'image shape: {img.shape}')