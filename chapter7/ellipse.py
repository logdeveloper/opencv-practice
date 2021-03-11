import cv2 as cv
import numpy as np

width = 640
height = 480
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)

center = (int(width/2), int(height/2))

# case1
# 노란색 타원
# cv.ellipse(img, center, (200, 10), 0, 0, 360, (0, 255, 255), 3)

# 초록색 타원
# cv.ellipse(img, center, (10, 200), 0, 0, 360, (0, 255, 0), 3)

# 빨간색 원
# cv.ellipse(img, center, (200, 200), 0, 0, 360, (0, 0, 255), 3)

# case2 : 타원 3개
# cv.ellipse(img, center, (10, 200), 0, 0, 360, (0, 255, 0), 3)
# cv.ellipse(img, center, (10, 200), 45, 0, 360, (0, 0, 255), 3)
# cv.ellipse(img, center, (10, 200), -45, 0, 360, (0, 255, 255), 3)

cv.ellipse(img, center, (100, 100), 0, 0, 120, (0, 0, 255), 3)

cv.imshow("result", img)
cv.waitKey(0)
