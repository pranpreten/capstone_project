import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread('images/Candies.png')

if image is None:
    print("이미지를 읽지 못했습니다. 파일 경로를 확인하세요.")
    exit()

# BGR 이미지를 HSV 색 공간으로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 붉은색 범위 지정 (HSV 범위)
# OpenCV에서 빨간색은 두 영역으로 나뉘어 있음 (0-10과 170-180)
lower_red1 = np.array([0, 120, 70])    # 첫 번째 빨간색 범위 (Hue: 0-10)
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])  # 두 번째 빨간색 범위 (Hue: 170-180)
upper_red2 = np.array([180, 255, 255])

# 각각의 범위에 대해 마스크 생성
mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)

# 두 마스크를 합침
red_mask = cv2.bitwise_or(mask1, mask2)

# 마스크를 원본 이미지에 적용하여 빨간색만 필터링
red_candies = cv2.bitwise_and(image, image, mask=red_mask)

# 결과 출력
cv2.imshow('Original Image', image)
cv2.imshow('Red Mask', red_mask)
cv2.imshow('Red Candies', red_candies)

cv2.waitKey(0)
cv2.destroyAllWindows()
