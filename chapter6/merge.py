import cv2 as cv
import numpy as np

img_logo = cv.imread('../sample/logo.png', cv.IMREAD_COLOR)
img_background = cv.imread('../sample/background.png', cv.IMREAD_COLOR)

img_gray = cv.cvtColor(img_logo, cv.COLOR_BGR2GRAY)
ret, img_mask = cv.threshold(img_gray, 200, 255, cv.THRESH_BINARY)

# 이진화 이미지도 필요
img_mask_inv = cv.bitwise_not(img_mask)

# 로고 이미지 크기만큼 배경 이미지를 잘라냄
# 로고가 삽입될 위치가 된다.
height, width = img_logo.shape[:2]
img_roi = img_background[0:height, 0:width]

# 이진화 이미지를 사용하여 로고 이미지에서는 배경을 지우고
# 배경 이미지에서는 로고가 들어갈 위치를 제거함.
img1 = cv.bitwise_and(img_logo, img_logo, mask=img_mask_inv)
img2 = cv.bitwise_and(img_roi, img_roi, mask=img_mask)

dst = cv.add(img1, img2)

img_background[0:height, 0:width] = dst

cv.imshow('backgroud', img_background)
cv.imshow('img_mask_inv', img_mask_inv)
cv.imshow('img_mask', img_mask)
cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('dst', dst)

cv.waitKey(0)