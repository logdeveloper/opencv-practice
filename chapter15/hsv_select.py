import cv2 as cv

cap = cv.VideoCapture(0)
if cap.isOpened() == False:
    print("카메라를 열 수 없습니다.")
    exit(1)

while(True):
    ret, img_frame = cap.read()
    if ret == False:
        print("캡쳐 실패")
        break

    # hsv 색공간으로 변환
    img_hsv = cv.cvtColor(img_frame, cv.COLOR_BGR2HSV)

    # 파란색 기준값을 120으로 상한, 하한값 정하기
    # 채도가 높은 파란색을 검출하기 때문에 HSV 색공간의 채도값을
    # 높여 채도가 낮은 파란색을 제거, 테스트에선 70을 사용
    lower_blue = (120-20, 70, 0)
    upper_blue = (120+20, 255, 255)
    # lower_blue = (0, 100, 20)
    # upper_blue = (255, 140,255)
    img_mask = cv.inRange(img_hsv, lower_blue, upper_blue)
    # 컬러영상에서 파란색만 보여줌
    img_result = cv.bitwise_and(img_frame, img_frame, mask=img_mask)

    cv.imshow('Color', img_frame)
    cv.imshow('Result', img_result)

    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()