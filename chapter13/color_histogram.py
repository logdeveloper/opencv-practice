import cv2 as cv
import numpy as np

src = cv.imread("../sample/apple.jpg", cv.IMREAD_COLOR)

bgr_planes = cv.split(src)

histSize = 256

histRange = (0, 256)

accumulate = False
# [0] : 히스토그램을 계산할 채널
# None : 마스크를 사용하지 않고, 모든 화소에서 히스토그램을 계산
# histSize : 히스토그램 hist(return)값의 각 빈(bin) 크기에 대한 정수 배열
# ranges : 히스토그램 각 빈의 경계값에 대한 배열
# accumulate : True이면 calcHist() 함수를 수행할 때, 히스토그램을 초기화 하지 않고 이전 값을 계속 누적.
b_hist = cv.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)
g_hist = cv.calcHist(bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate)
r_hist = cv.calcHist(bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate)

hist_w = 256*3
hist_h = 400

histImage = np.zeros((hist_h, hist_w,3), dtype=np.uint8)

cv.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(g_hist, g_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)
cv.normalize(r_hist, r_hist, alpha=0, beta=hist_h, norm_type=cv.NORM_MINMAX)

for i in range(0, histSize):
    # blue histogram
    cv.line(histImage,
            (i, hist_h-int(np.round(b_hist[i])) ),
            (i, hist_h-0) , (255, 0, 0), thickness=2 )

    # green histogram
    cv.line(histImage,
            (i + 256, hist_h-int(np.round(g_hist[i-1])) ),
            (i+256, hist_h-0) , (0,255, 0), thickness=2 )

    # red histogram
    cv.line(histImage,
            (i + 256*2, hist_h - int(np.round(r_hist[i-1])) ),
            (i+ 256*2, hist_h - 0), (0, 0, 255), thickness=2)

# 결과 보여주기
cv.imshow("source image", src)
cv.imshow("Histogram", histImage)

cv.waitKey()