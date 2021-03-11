import cv2 as cv

img_gray = cv.imread('../test.jpg', cv.IMREAD_GRAYSCALE)

# copy 만들기
img_copyed1 = img_gray.copy()

# 둘의 데이터를 공유하는지 리턴 값으로 체크
print(id(img_gray), id(img_copyed1))

cv.line(img_gray, (0,0), (100, 100), 0, 10)

ret, img_sub1 = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

print(id(img_gray), id(img_copyed1))

cv.imshow("img_gray", img_gray)
cv.imshow("img_sub1", img_sub1)

cv.waitKey(0)