# Hough Line Transform : 직선을 찾기 위해 사용되는 알고리즘

import math
import cv2 as cv
import numpy as np

img_src = cv.imread("../sample/houseline.jpg", cv.IMREAD_GRAYSCALE)
img_edge = cv.Canny(img_src, 50, 150)
img_result = cv.cvtColor(img_edge, cv.COLOR_GRAY2BGR)
img_result_2 = cv.cvtColor(img_edge, cv.COLOR_GRAY2BGR)

img_result_P = np.copy(img_result)
img_result_P_2 = np.copy(img_result)
lines = cv.HoughLines(img_edge, 1, np.pi/180, 150)
linesP = cv.HoughLinesP(img_edge, 1, np.pi/180, 50, None, 50, 5)

if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)

        x0 = a*rho
        y0 = b*rho

        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000*(a)))

        cv.line(img_result, pt1, pt2, (0,0,255), 3)

cv.imshow("Source", img_src)
cv.imshow("Standard Hough Line Transform", img_result)

if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv.line(img_result_P_2, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)

cv.imshow("Probilistic Line Transform", img_result_P_2)

cv.waitKey()