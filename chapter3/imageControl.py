import cv2 as cv

img_gray = cv.imread('../test.jpg', cv.IMREAD_GRAYSCALE)

img_copyed1 = img_gray

#  img_copyed1, img_gray의 datatype은 numpy 배열
# id return 값이 동일함.
print(id(img_gray), id(img_copyed1))

cv.line(img_gray, (0,0), (100, 100), 0, 10)

# 이진화 적용 하여 img_gray에 저장
ret, img_gray = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)

# 이제 둘은 다른 객체가 됨.
print(id(img_gray), id(img_copyed1))

cv.imshow("img_gray", img_gray)

cv.imshow("img_copyed1", img_copyed1)

cv.waitKey(0)