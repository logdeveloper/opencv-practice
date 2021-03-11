import cv2 as cv

#cap = cv.VideoCapture(0)
# window 에러 해결하기 위해 옵션 추가
cap = cv.VideoCapture(0, cv.CAP_DSHOW)


if cap.isOpened() == False:
    print("카메라를 열 수 없습니다.")
    exit(1)

ret, img_frame = cap.read()

if ret == False:
    print("캡쳐 실패")
    exit(1)

# 코덱 설정
#codec = cv.VideoWriter_fourcc('M','J','P','G')
# window는 divx
codec = cv.VideoWriter_fourcc(*'DIVX')

# 프레임 레이트 (frame rate)
fps = 300

h, w = img_frame.shape[:2]

writer = cv.VideoWriter("output.avi", codec, fps, (w,h))

if writer.isOpened() == False:
    print("동영상 파일을 준비할 수 없습니다.")
    exit(1)

# 캡쳐한 것을 반복적으로 보여주기
while(True):
    ret, img_frame = cap.read()

    if ret == False:
        print("캡쳐 실패")
        break;

    writer.write(img_frame)

    cv.imshow('Color', img_frame)

    key = cv.waitKey(1)

    if key == 27:
        break

cap.release()

#저장하기 위해 VideoWriter객체에 릴리즈 함.
writer.release()

cv.destroyAllWindows()



