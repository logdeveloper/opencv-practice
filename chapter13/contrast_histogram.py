# histogram equalization :  이미지 밝기가 알맞지 않은 경우 히스토그램을 전체 영역에 고루 퍼져 있도록 바꾸어 이미지 개선.
# 얼굴 데이터를 훈련시키기 전에 같은 조명 상태로 만드릭 위해 사용
# 히스토그램 평활화를 적용하면 오른쪽처럼 거의 같은 밝기, 대비의 이미지를 얻을 수 있음.

import cv2 as cv
import numpy as np

def draw_histogram(img) :

    # 히스토그램을 그릴 이미지를 생성
    hist_h = img.shape[0]
    hist_w = 256
    img_histogram1 = np.zeros( (hist_h, hist_w, 1), dtype=np.uint8 )

    # 히스토그램 계산하여 그리기
    histSize = 256
    histRange = (0,256)
    accumulate = False
    hist_item = cv.calcHist([img], [0], None, [histSize], histRange, accumulate=accumulate)

    cv.normalize(hist_item, hist_item, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)

    for i in range(0, histSize):
        cv.line(img_histogram1, (i, hist_h-int(np.round(hist_item[i]))),
                (i, hist_h), (255,255,255))

    # 누적 히스토그램을 그릴 이미지를 생성
    img_histogram2 = np.zeros( (hist_h, hist_w, 1) , dtype=np.uint8)
    c_hist = np.zeros(hist_item.shape, dtype=hist_item.dtype)

    c_hist[0] = hist_item[0]
    for i in range(1, hist_item.shape[0]):
        c_hist[i] = hist_item[i] + c_hist[i-1]

    cv.normalize(c_hist, c_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)

    for i in range(1, histSize):
        pts = []
        pts.append( (i, hist_h-np.round(c_hist[i])) )
        pts.append(((i-1), hist_h - np.round(c_hist[i-1])))
        pts = np.array(pts)
        pts = np.int32(pts)
        cv.polylines(img_histogram2, [pts], False, (255,255,255))

    result = cv.hconcat((img_histogram1, img_histogram2))

    return result

img_gray = cv.imread("../sample/frog.png", cv.IMREAD_GRAYSCALE)

img_histo1 = draw_histogram(img_gray)

result1 = cv.hconcat((img_gray, img_histo1))

cv.imshow('result1', result1)

img_equ = cv.equalizeHist(img_gray)
img_histo2 = draw_histogram(img_equ)
result2 = cv.hconcat((img_equ, img_histo2))
cv.imshow('result2', result2)

cv.waitKey(0)
cv.destroyAllWindows()
