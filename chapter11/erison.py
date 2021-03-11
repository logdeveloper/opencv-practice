import cv2 as cv
import numpy as np

img_gray = cv.imread('../sample/test_i.png', cv.IMREAD_GRAYSCALE)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))

# 선의 굵기를 얇게
img_result = cv.erode(img_gray, kernel, iterations=1)

img_result2 = cv.dilate(img_gray, kernel, iterations=1)

cv.imshow('input', img_gray)
cv.imshow('erode', img_result)
cv.imshow('dilate', img_result2)

cv.waitKey(0)
cv.destroyAllWindows()
