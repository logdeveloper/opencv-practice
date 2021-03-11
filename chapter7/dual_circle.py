import cv2 as cv
import numpy as np

width = 640
height = 480
bpp = 3

img = np.zeros((height, width, 3), np.uint8)

img_h = img.shape[0]
img_w = img.shape[1]
img_bpp = img.shape[2] # 채널수


# 원 그리기
cv.circle(img, (320, 240), 10, (0, 255, 0), -1)

# 선굵기가 1인 원 그리기
cv.circle(img, (320, 240), 100, (0, 0, 255), 1)

cv.imshow("drawing", img)

cv.waitKey(0)

