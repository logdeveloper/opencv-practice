import cv2 as cv
import sys


img_color = cv.imread('../sample/orange.png', cv.IMREAD_COLOR)

if img_color is None:
    print("이미지 파일을 읽을수 없습니다.")
    sys.exit(1)

img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

img_canny = cv.Canny(img_gray, 90, 180)

# 두개의 사진이 따로 나오는 출력
# cv.imshow('GrayScale', img_gray)
# cv.imshow('Canny', img_canny)

# 수평 방향으로 matrics에 포함된 이미지를 연결
img_result = cv.hconcat([img_gray, img_canny])

# 수직 방향으로 matrics에 포함된 이미지를 연결
# img_result = cv.vconcat([img_gray, img_canny])

cv.imshow('Result', img_result)

cv.waitKey(0)
cv.destroyAllWindows()