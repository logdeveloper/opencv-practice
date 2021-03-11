import cv2 as cv
import numpy as np

width = 640
height = 480
bpp = 3

img = np.zeros((height, width, 3), np.uint8)

# 빨간색 선 굵기가 3인 사각형
cv.rectangle(img, (50,50), (450, 450), (0, 0, 255), 3)

# 초록색으로 그려진 사각형
cv.rectangle(img, (100,150), (250, 300), (0, 255, 0), -1)

# 마젠타 색으로 그려진 사각형
cv.rectangle(img, (300, 150, 50, 100), (255, 0, 255), -1)


# 원 그리기

cv.imshow("result", img)

cv.waitKey(0)

