import cv2 as cv
import numpy as np

width = 640
height = 640
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)

red = (0,0,255)
green = (0, 252, 0)
yellow = (0, 255, 255)

thickness = 2

# 1. 바깥 오각형
pts = np.array([[315, 50],[570,240],[475,550],
                [150,550],[50,240]], np.int32)

pts = pts.reshape((-1, 1, 2))

# False, 시작과 끝이 이어지지 않음.
cv.polylines(img, [pts], False, red, thickness)

# 2. 중간 오각형
pts = np.array([[315, 160],[150,280],[210,480],
                [420,480],[480,280]], np.int32)
pts = pts.reshape((-1, 1, 2))
# False, 시작과 끝이 이어지지 않음.
cv.polylines(img, [pts], False, green, thickness)


# 2. 제일 안쪽 오각형
pts = np.array([[320, 245],[410,315],[380,415],
                [265,415],[240,315]], np.int32)
pts = pts.reshape((-1, 1, 2))
# False, 시작과 끝이 이어지지 않음.
cv.fillPoly(img, [pts], yellow)

cv.imshow("drawing", img)
cv.waitKey(0)