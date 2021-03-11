import cv2 as cv
import numpy as np

# 우선 dummy함수로 지정
def on_trackbar(x):
    pass

# 트랙바를 붙일 윈도우 생성
cv.namedWindow('Canny')

# 트랙바 생성
cv.createTrackbar('low threshold', 'Canny', 0, 1000, on_trackbar)
cv.createTrackbar('high threshold', 'Canny', 0, 1000, on_trackbar)

# 트랙바 초기화
cv.setTrackbarPos('low threshold', 'Canny', 50)
cv.setTrackbarPos('high threshold', 'Canny', 150)

# 이미지는 그레이 스케일로 불러옴git

img_gray = cv.imread('../sample/finger.jpg', cv.IMREAD_GRAYSCALE)

while(1):
    low = cv.getTrackbarPos('low threshold', 'Canny')
    high = cv.getTrackbarPos('high threshold', 'Canny')

    img_canny = cv.Canny(img_gray, low, high)

    cv.imshow('Canny', img_canny)

    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()



# GUI를 통해서 트랙바를 조정 가능하다.