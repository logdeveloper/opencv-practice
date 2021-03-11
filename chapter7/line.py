import cv2 as cv
import numpy as np

width = 640
height = 480
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)

img_h = img.shape[0]
img_w = img.shape[1]
img_bpp = img.shape[2] # 채널수


# 원 그리기
cv.line(img, (width-1, 0), (0, height-1), (0, 255, 0), 3)
cv.line(img, (0, 0), (width-1, height-1), (0, 0, 255), 3)

cv.imshow("result", img)

cv.waitKey(0)

