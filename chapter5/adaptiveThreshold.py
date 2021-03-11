import cv2 as cv
import sys

# 적응형 이진화 Adaptive thresholding : 이미지를 작은 영역으로 나누어 각 영역별로 다른 임계값을 적용

img_color = cv.imread("../sample/copy_paper.png", cv.IMREAD_COLOR)

if img_color is None:
    print("이미지 파일을 읽어올 수 없습니다.")
    sys.exit(1)

img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

img_binary = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                  cv.THRESH_BINARY, 5,4)

img_result = cv.vconcat([img_gray, img_binary])

cv.imshow('result', img_result)


cv.waitKey(0)
