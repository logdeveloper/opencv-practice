import cv2 as cv
import numpy as np

src = np.zeros([4,2], dtype=np.float32)
idx = 0

def mouse_callback(event, x, y, flags, params):
    global point_list, idx

    if event == cv.EVENT_LBUTTONDOWN:
        src[idx] = (x,y)
        idx = idx +1

        print("(%d %d)" % (x,y))

        cv.circle(img_color, (x,y), 10, (0,0,255), -1)

cv.namedWindow('original')
cv.setMouseCallback('original', mouse_callback)

img_color = cv.imread('../sample/road.jpg')
img_original = img_color.copy()

while(True):
    cv.imshow('original', img_color)
    height, width = img_color.shape[:2]

    if cv.waitKey(1) ==32:
        break

dst = np.float32( [[0,0], [width, 0], [0, height], [width, height]] )

M = cv.getPerspectiveTransform(src, dst)

img_result = cv.warpPerspective(img_original, M, (width, height))

cv.imshow("result1", img_result)
cv.waitKey(0)
cv.destroyAllWindows()