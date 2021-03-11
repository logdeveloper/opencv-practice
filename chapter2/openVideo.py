import cv2 as cv

#cap = cv.VideoCapture(0)
# window 에러 해결하기 위해 옵션 추가
cap = cv.VideoCapture(0, cv.CAP_DSHOW)


if cap.isOpened() == False:
    print("카메라를 열 수 없습니다.")
    exit(1)

# 캡쳐한 것을 반복적으로 보여주기
while(True):
    ret, img_frame = cap.read()

    if ret == False:
        print("캡쳐 실패")
        break;

    cv.imshow('Color', img_frame)

    key = cv.waitKey(1)

    if key == 27:
        break

cap.release()
cv.destroyAllWindows()
