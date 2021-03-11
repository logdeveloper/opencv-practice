# Hough Line Transform : 직선을 찾기 위해 사용되는 알고리즘

import math
import cv2 as cv
import numpy as np

# img_gray = cv.imread("../sample/circle.jpg", cv.IMREAD_GRAYSCALE)
img_gray = cv.imread("../sample/orange.png", cv.IMREAD_GRAYSCALE)
img_gray = cv.medianBlur(img_gray, 5)

img_color = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)

circles = cv.HoughCircles(img_gray, cv.HOUGH_GRADIENT, 1, 20,
                          param1=50, param2=35, minRadius= 0, maxRadius=0)
circles = np.uint16(np.around(circles))

for c in circles[0,:]:
    center = (c[0], c[1])
    radius = c[2]

    cv.circle(img_color, center, radius, (0,255,0), 2)
    cv.circle(img_color, center, 2, (0,255,0), 3 )

cv.imshow('detected circles', img_color)
cv.waitKey()
cv.destroyAllWindows()