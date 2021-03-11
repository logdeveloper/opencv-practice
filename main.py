import cv2

img_color = cv2.imread("test.png", cv2.IMREAD_COLOR)

if img_color is None:
    print("이미지 파일을 읽을 수 없습니다.")
    exit()

cv2.namedWindow('Color')
cv2.imshow('Color', img_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
