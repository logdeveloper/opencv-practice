# 라벨링은 이진화 영상으로 바꾼 후, 각 흰색 영역을 구분하기 위해 영역마다 번호를 부여하는 것.
# 라벨링을 하면 한 장의 이미지에 있는 흰색 영역들을 개별적으로 다룰 수 있음.

import cv2 as cv

img_color = cv.imread('../sample/plus.jpg', cv.IMREAD_COLOR)
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

cv.imshow('result', img_gray)
cv.waitKey(0)

# canny 함수를 통해 에지 검출
img_edge = cv.Canny(img_gray, 50, 150)
cv.imshow('result1', img_edge)
cv.waitKey(0)

# 관심 물체가 흰색이 되어야 하므로 반전시킴
img_edge = cv.bitwise_not(img_edge)
cv.imshow('result2', img_edge)
cv.waitKey(0)

# 컨투어를 찾아서 외각선을 보강
contours = cv.findContours(img_edge.copy(), cv.RETR_LIST,
                           cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img_edge, contours[0], -1, (0,0,0), 1)
cv.imshow('result3', img_edge)
cv.waitKey(0)

# 흰색 영역에 대해 라벨링
nlabels, labels, stats, centroids = cv.connectedComponentsWithStats(img_edge)

for i in range(nlabels):
    # 배경은 제외
    if i < 2:
        continue
    # 흰색 영역의 크기, 중심 좌표, 외각 사각형에 대한 정보를 가져옴
    area = stats[i, cv.CC_STAT_AREA]
    center_x = int(centroids[i,0])
    center_y = int(centroids[i,1])
    left = stats[i, cv.CC_STAT_LEFT]
    top = stats[i, cv.CC_STAT_TOP]
    width = stats[i, cv.CC_STAT_WIDTH]
    height = stats[i, cv.CC_STAT_HEIGHT]

    # 영역의 크기가 50 이상인 경우 다음과 같은 정보 표시
    if area > 50:
        # 사각형 그리기
        cv.rectangle(img_color, (left, top), (left + width, top +  height),
                     (0,0,255), 1)
        # 원 그리기
        cv.circle(img_color, (center_x, center_y), 5, (255,0,0),1)

        # 라벨 번호를 표시
        cv.putText(img_color, str(i), (left+20, top+20),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)

# 결과를 화면에 보여줌.
cv.imshow('result4', img_color)
cv.waitKey(0)