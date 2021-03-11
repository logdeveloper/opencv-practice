# meanshift : 물체를 추적할 때 사용할 수 있는 알고리즘,

import cv2 as cv

mouse_is_pressing = False
start_x, start_y, end_x, end_y = -1,-1,-1,-1
step = 0
track_window = None

def mouse_callback(event, x, y, flags, param):
    global start_x, start_y, end_x, end_y
    global step, mouse_is_pressing, track_window

    # 왼쪽 버튼을 누를 시 현재 좌표를 사각형으로 그릴때 시작좌표를 저장
    if event == cv.EVENT_LBUTTONDOWN:
        step = 1
        mouse_is_pressing = True
        start_x = x
        start_y = y

    # 왼쪽 버튼을 누른 채 마우스 이동 시 현재 좌표를 사각형을 그릴때 끝 좌표를 저장
    elif event == cv.EVENT_MOUSEMOVE:
        if mouse_is_pressing:
            end_x = x
            end_y = y

            step = 2

    # 왼쪽 버튼에서 손을 땔때의 좌표를 사각형 그릴 때 끝 좌표로 저장.
    elif event == cv.EVENT_LBUTTONUP:
        mouse_is_pressing = False

        end_x = x
        end_y = y

        step = 3

# 웹캠을 초기화
cap = cv.VideoCapture(0)

if cap.isOpened() == False:
    print("카메라를 열 수 없습니다.")
    exit(1)

# 윈도우를 생성하고 마우스 콜백함수를 설정
cv.namedWindow("color")
cv.setMouseCallback("color", mouse_callback)

while(True):

    ret, img_color = cap.read()

    if ret == False:
        print("캡쳐 실패")
        break

    if step == 1: # 처음 클릭 시 원을 보여줌
        cv.circle(img_color, (start_x, start_y), 10,
                  (0,255,0), -1)
    elif step == 2: # 마우스 이동 중 사각형을 그려줌
        cv.rectangle(img_color, (start_x, start_y),
                     (end_x, end_y), (0,255,0), 3)
    elif step == 3: # 손을 뗀 경우 ROI 영역을 얻게 됨
        if start_x > end_x:
            start_x, end_x = end_x, start_x
            start_y, end_y = end_y, start_y

        track_window = (start_x, start_y, end_x-start_x, end_y-start_y)
        img_hsv = cv.cvtColor(img_color, cv.COLOR_BGR2HSV)
        img_ROI = img_hsv[start_y:end_y, start_x:end_x]
        cv.imshow("ROI", img_ROI)
        objectHistogram = cv.calcHist([img_ROI], [0], None, [180],(0,180))

        cv.normalize(objectHistogram, objectHistogram, alpha=0, beta=255,
                     norm_type= cv.NORM_MINMAX)

        step = step+1

    elif step == 4:
        img_hsv = cv.cvtColor(img_color, cv.COLOR_BGR2HSV)
        bp = cv.calcBackProject([img_hsv], [0], objectHistogram,
        [0,180], 1)

        ret, track_window = cv.meanShift(bp, track_window,
                                         (cv.TERM_CRITERIA_EPS | cv.TermCriteria_COUNT, 10,1))

        x,y,w,h = track_window
        cv.rectangle(img_color, (x,y), (x+w, y+h), (0,0,255), 2)

    cv.imshow('color', img_color)

    if cv.waitKey(25) >= 0 :
        break
