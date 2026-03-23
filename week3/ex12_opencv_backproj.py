import cv2

# 이미지 읽기
src = cv2.imread('images/desert.jpg', cv2.IMREAD_COLOR)

if src is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
    exit()

# ROI 선택 (마우스로 영역 선택 후 Enter/Space)
x, y, w, h = cv2.selectROI(src)

# BGR -> YCrCb 색 공간 변환
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

# 선택한 ROI 영역
roi = src_ycrcb[y:y+h, x:x+w]

# ROI의 히스토그램 계산
hist = cv2.calcHist([roi], [1, 2], None, [128, 128], [0, 256, 0, 256])

# 히스토그램 역투영
backproj = cv2.calcBackProject([src_ycrcb], [1, 2], hist, [0, 256, 0, 256], 1)

# 마스크를 적용하여 해당 영역만 추출
dst = cv2.copyTo(src, backproj)

# 결과 출력
cv2.imshow('BackProject', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
