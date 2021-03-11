import cv2

# numpy객체로 반환, (행,열, 색상 : 기본 B, G, R)
img_color = cv2.imread("../test.jpg", cv2.IMREAD_COLOR)

if img_color is None:
    print("이미지 파일을 읽을 수 없습니다.")
    exit()

#컬러 이미지 보여주기
cv2.namedWindow('Color')
cv2.imshow('Color', img_color)

# 대기하고 있다가, 키보드 입력이 있으면 다음줄 실행
cv2.waitKey(0)

# 그레이 스케일로 변환
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# 이미지 팝업창으로 띄우기
cv2.imshow('GrayScale', img_gray)

# 특정한 이미지를 파일로 저장하는 함수
cv2.imwrite('grayscale.jpg', img_gray)

# 키보드 입력을 처리하는 함수
# time : 입력 대기 시간(무한대기:0)
# 반환값 : 사용자가 입력한 AsciiCode(ESC:27)
cv2.waitKey(0)
# 화면의 모든 윈도우를 모두 닫는것.
cv2.destroyAllWindows()

