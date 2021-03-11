# 템플릿 매칭 : 주어진 템플릿 이미지와 일치하는 영역을 입력 이미지에서 찾는 방법

import cv2 as cv
import numpy as np

# 이미지 불러오기
img_rgb = cv.imread('../sample/all.jpg')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

def notInList(newObject) :
    for detectedObject in detectedObjects:
        a = newObject[0] - detectedObject[0]
        b = newObject[1] - detectedObject[1]
        if np.sqrt(a*a + b*b) < 5 :
            return False
    return True

detectedObjects = []

img_rgb = cv.imread("../sample/all.jpg")
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
img_template = cv.imread('../sample/template.jpg', cv.IMREAD_GRAYSCALE)
w, h = img_template.shape[:2]

# 템플릿 매칭
res = cv.matchTemplate(img_gray, img_template, cv.TM_CCOEFF_NORMED)

count = 0


for x in range(res.shape[1]):
    for y in range(res.shape[0]):
        # 임계값이 0.9보다 크고, 기존에 템플림 검출 리스트에 포함된 좌표가 5이상이어야
        # 새로운 리스트에 추가함.
        index = str(x)+"_"+str(y)

        if res[y,x] > 0.9 and notInList((x,y)):
            detectedObjects.append((x,y))
            cv.rectangle(img_rgb, (x,y), (x+w, y+h), [0,0,255], 1)
            print(index)
            cv.imshow('result_'+index, img_rgb)
            count = count+1

print(count)
cv.imshow('result', img_rgb)
cv.waitKey(0)