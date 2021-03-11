import cv2 as cv

img_color = cv.imread('../sample/test.jpg')
cv.imshow("color",img_color)

height, width = img_color.shape[:2]

M = cv.getRotationMatrix2D((width/2.0, height/2.0),
                           45, 1)

img_rotated = cv.warpAffine(img_color, M, (width, height))

cv.imshow('rotation', img_rotated)
cv.waitKey(0)

cv.destroyAllWindows()