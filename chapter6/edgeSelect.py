import cv2 as cv

img_color = cv.imread('../sample/orange.png')

height, width = img_color.shape[:2]
center_x , center_y = int(width*0.5), int(height*0.5)

img_roi = img_color[center_y-100:center_y+100, center_x-100:center_x+100].copy()

img_gray = cv.cvtColor(img_roi, cv.COLOR_BGR2GRAY)
img_edge = cv.Canny(img_gray, 100, 300)

img_edge = cv.cvtColor(img_edge, cv.COLOR_GRAY2BGR)

# 원본 컬러영상에 다시 ROI 컬러 영상으로 변환
img_color[center_y-100:center_y+100, center_x-100:center_x+100] = img_edge

cv.imshow('COLOR', img_color)
cv.imshow('ROI', img_roi)

cv.waitKey(0)
cv.destroyAllWindows()

