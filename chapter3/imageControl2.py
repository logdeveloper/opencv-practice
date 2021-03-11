import cv2 as cv

img_gray = cv.imread('../test.jpg', cv.IMREAD_GRAYSCALE)

# ROI : Region of Interest 이미지 일부를 지정
# [start_y:end_y, start_x, end_y]로 ROI 영역을 지정
img_sub1 = img_gray[20:20+150, 20:20+150]

# 둘의 데이터를 공유하는지 리턴 값으로 체크
print(img_sub1.base is img_gray)

cv.line(img_gray, (0,0), (100, 100), 0, 10)

ret, img_sub1 = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

print(img_sub1.base is img_gray)

cv.imshow("img_gray", img_gray)
cv.imshow("img_sub1", img_sub1)

cv.waitKey(0)