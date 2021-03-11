import cv2 as cv
import sys

def on_trackbar(x):
    pass

cv.namedWindow('Canny')

# 트랙바 생성
cv.createTrackbar('low threshold', 'Canny', 0, 1000, on_trackbar)
cv.createTrackbar('high threshold', 'Canny', 0, 1000, on_trackbar)

# 트랙바 초기화
cv.setTrackbarPos('low threshold', 'Canny', 50)
cv.setTrackbarPos('high threshold', 'Canny', 150)

img_color = cv.imread('../sample/orange.png', cv.IMREAD_COLOR)

if img_color is None:
    print("이미지 파일을 읽을수 없습니다.")
    sys.exit(1)

img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)



# 두개의 사진이 따로 나오는 출력
# cv.imshow('GrayScale', img_gray)
# cv.imshow('Canny', img_canny)

while(1):
    low = cv.getTrackbarPos('low threshold', 'Canny')
    high = cv.getTrackbarPos('high threshold', 'Canny')

    img_canny = cv.Canny(img_gray, low, high)


    # cv.imshow('Canny', img_canny)

    if cv.waitKey(1) & 0xFF == 27:
        break

    # # 수평 방향으로 matrics에 포함된 이미지를 연결
    # img_result = cv.hconcat([img_gray, img_canny])

    #수직 방향으로 matrics에 포함된 이미지를 연결
    img_result = cv.vconcat([img_gray, img_canny])

    cv.imshow('Canny', img_result)

cv.waitKey(0)
cv.destroyAllWindows()