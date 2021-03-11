import cv2 as cv
import numpy as np
import random

# 마우스 왼쪽 버튼 체크 상태
mouse_is_pressing = False
# 현재 그리기 모드 선택을 위해 사용(원/사각형)
drawing_mode = True
# 최초로 마우스 왼쪽 버튼 누른 위치를 저장하기 위해 사용
start_x, start_y = -1, -1
# 도형 내부를 채울 때 사용할 색 지정 시 사용
color = (255,255,255)
# 그리기 결과를 저장할 이미지
img = np.zeros((512, 512, 3), np.uint8)

def mouse_callback(event, x, y, flags, params):

    global color,start_x, start_y, drawing_mode, mouse_is_pressing

    # 1. 마우스를 이동하면
    if event == cv.EVENT_MOUSEMOVE :
        if mouse_is_pressing == True:
            cv.rectangle(img, (start_x, start_y), (x,y), color, -1)

        else:
            cv.circle(img, (start_x, start_y), max(abs(start_x-x),
                                                   abs(start_y-y)), color, -1)
    # 2. 왼쪽 버튼을 누르면
    elif event==cv.EVENT_LBUTTONDOWN:
        color = (random.randrange(256), random.randrange(256),random.randrange(256))
        mouse_is_pressing=True
        start_x, start_y = x,y

    # 3. 누르고 있는 마우스 왼쪽 버튼에서 손을 떼면 발생하는 이벤트
    elif event == cv.EVENT_LBUTTONUP:
        mouse_is_pressing == False
        if drawing_mode == True:
            if mouse_is_pressing == True:
                cv.rectangle(img, (start_x, start_y), (x, y), color, -1)

            else:
                cv.circle(img, (start_x, start_y), max(abs(start_x - x),
                                                       abs(start_y - y)), color, -1)

    # 4. 오른쪽 버튼을 누르면
    elif event == cv.EVENT_RBUTTONDOWN:
        drawing_mode = 1 - drawing_mode

cv.namedWindow('image')

# 지정한 윈도우를 위한 마우스 콜백함수를 지정
cv.setMouseCallback('image', mouse_callback)

while(1):
    cv.imshow('image', img)
    key=cv.waitKey(1)
    if key == 27:
        break

cv.destroyAllWindows()


