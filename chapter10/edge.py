import cv2 as cv

# img_color = cv.imread('../sample/box.png', cv.IMREAD_COLOR)
# img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
#
# img_sobel_x = cv.Sobel(img_gray, cv.CV_64F, 1, 0, ksize=3)
# img_sobel_x = cv.convertScaleAbs(img_sobel_x)
#
#
# img_sobel_y = cv.Sobel(img_gray, cv.CV_64F, 0, 1, ksize=3)
# img_sobel_y = cv.convertScaleAbs(img_sobel_y)
#
# img_sobel = cv.addWeighted(img_sobel_x, 1, img_sobel_y, 1, 0)
#
# cv.imshow("sobel_x", img_sobel_x)
# cv.imshow("sobel_y", img_sobel_y)
# cv.imshow("sobel", img_sobel)


img_gray = cv.imread('../sample/house.png', cv.IMREAD_GRAYSCALE)
cv.imshow('original', img_gray)

img_gray = cv.blur(img_gray, (3,3))
img_canny = cv.Canny(img_gray, 50, 150)
cv.imshow('canny edge', img_canny)

cv.waitKey(0)
cv.destroyAllWindows()



cv.waitKey(0)
cv.destroyAllWindows()
