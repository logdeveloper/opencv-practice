import cv2 as cv
import numpy as np

width = 640
height = 480

img = np.zeros((height, width, 3), np.uint8)

img_h = img.shape[0]
img_w = img.shape[1]
img_bpp = img.shape[2] # 채널수

print(img_h, img_w, img_bpp)

# 원 그리기
cv.circle(img, (200, 100), 10, (0, 255, 255), -1)

cv.imshow("drawing", img)

cv.waitKey(0)

