import cv2 as cv
import sys

def on_trackbar(x):
    pass

img_color = cv.imread("../sample/test.jpg", cv.IMREAD_COLOR)

if img_color is None:
    print("이미지 파일을 읽을 수 없습니다.")
    sys.exit(1)

img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)


# Binary 트랙바 추가
cv.namedWindow('Binary')

# 트랙바 생성
cv.createTrackbar('threshold', 'Binary', 0, 255, on_trackbar)
cv.setTrackbarPos('threshold', 'Binary', 127)

while(True):

    thresh = cv.getTrackbarPos("threshold", "Binary")

    retval, img_binary = cv.threshold(img_gray, thresh, 255, cv.THRESH_BINARY_INV)

    img_result = cv.hconcat([img_gray, img_binary])

    cv.imshow('Binary', img_result)

    if cv.waitKey(1) & 0XFF == 27:
        break