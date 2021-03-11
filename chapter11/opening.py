import cv2 as cv
import numpy as np

img_gray = cv.imread('../sample/test_i2.png', cv.IMREAD_GRAYSCALE)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))

# 노이즈를 제거하는데 사용

img_result = cv.morphologyEx(img_gray, cv.MORPH_OPEN, kernel)

cv.imshow("input", img_gray)
cv.imshow("result", img_result)

cv.waitKey(0)
cv.destroyAllWindows()
