import cv2 as cv

img_color = cv.imread('../sample/figure.jpg', cv.IMREAD_COLOR)

# 그레이 스케일로 변환 후, 이진화하여 바이너리 이미지로 변환
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY_INV)

# 이진화 결과를 개선하기 위해 모폴로지 연산을 해줌
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
img_binary = cv.morphologyEx(img_binary, cv.MORPH_CLOSE, kernel)

# 컨투어를 검출
contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST,
                                      cv.CHAIN_APPROX_SIMPLE)

# 검출된 2개의 컨투어를 이미지에 그려줌. 인덱스 0,1에 저장
cv.drawContours(img_color, contours, 0, (0,0,255), 3)
cv.drawContours(img_color, contours, 1, (0,255,0), 3)

# conturArea 함수 사용
# for i, contours in enumerate(contours):
#     area = cv.contourArea(contours )

cv.imshow("result", img_color)
cv.waitKey(0)
