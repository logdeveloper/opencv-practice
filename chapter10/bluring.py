import cv2 as cv
import numpy as np

img = cv.imread('../sample/affine.png')
img2 = cv.imread('../sample/median.png')

kernel = np.ones((5,5), np.float32)/25
dst = cv.filter2D(img, -1, kernel)

# img_blur = cv.blur(img, (5,5))

img_blur = cv.GaussianBlur(img, (5,5), 0)

median = cv.medianBlur(img2, 5)

img3 = cv.imread('../sample/texture.png')

bilateral_blur = cv.bilateralFilter(img3, 9, 75, 75)

cv.imshow('original', img)

cv.imshow('result', dst)

cv.imshow('gaussizn blur', img_blur)

cv.imshow('megian blur', median)

cv.imshow('bilateral blur', bilateral_blur)

cv.waitKey(0)
cv.destroyAllWindows()
