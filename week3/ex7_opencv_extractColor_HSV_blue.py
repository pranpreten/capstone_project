import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread('images/Candies.png')

if image is None:
    print("이미지를 읽지 못했습니다. 파일 경로를 확인하세요.")
    exit()

# BGR 이미지를 HSV 색 공간으로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 파란색 범위 지정 (HSV 범위)
# [힌트] 파란색 영역은 Hue (100-140)
lower_blue = np.array([100, 120, 70])
upper_blue = np.array([140, 255, 255])

# 마스크 생성
blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# 마스크를 원본 이미지에 적용하여 파란색만 필터링
blue_candies = cv2.bitwise_and(image, image, mask=blue_mask)

# 결과 출력
cv2.imshow('Original Image', image)
cv2.imshow('Blue Mask', blue_mask)
cv2.imshow('Blue Candies', blue_candies)

cv2.waitKey(0)
cv2.destroyAllWindows()
