import cv2 as cv
import numpy as np

img_color = cv.imread('../test.jpg', cv.IMREAD_COLOR)

# 이미지의 높이와 너비를 가져옴
print("img datatype", type(img_color))
print("real values  : ", img_color)
height, width = img_color.shape[:2]
print("height : ", height, ", width : ", width)

# 그레이 스케일 이미지 저장할 넘파이 배열 생성
img_gray = np.zeros( (height, width), np.uint8)

for y in range(0, height):
    for x in range ( 0, width):
        # rgb 값을 읽어옴
        b = img_color.item(y,x,0)
        g = img_color.item(y, x, 1)
        r = img_color.item(y, x, 2)

        # (x,y) 위치의 픽셀에 그레이 스케일이 저장
        # 평균값을 사용하는 경우
        gray = int((r+g+b) / 3.0)
        # BT.709에 명시된 비율 사용하는 경우
        # gray = int(r*0.2126 + g*0.7152, b*0.0722)

        img_gray.itemset(y, x, gray)

# 결과를 컬러로 변경
img_result = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)

# y범위가 150~200, x범위가 200~250인 영역의 픽셀 색상 변경
for y in range(150,201):
    for x in range ( 200,250):
        #  초록색으로 변경
        img_result.itemset(y, x, 0, 0)
        img_result.itemset(y, x, 1, 255)
        img_result.itemset(y, x, 2, 0)

cv.imshow('color', img_color)
cv.imshow('result', img_result)

cv.waitKey(0)

cv.destroyAllWindows()