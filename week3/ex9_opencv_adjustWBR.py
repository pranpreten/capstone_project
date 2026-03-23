import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지를 그레이스케일로 읽기
image = cv2.imread('images/Lenna.png', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
    exit()

# 명암비 조작
alpha = 1.0
func = (1 + alpha) * image - (alpha * 128)
dst = np.clip(func, 0, 255).astype(np.uint8)

# 원본 및 결과 이미지 출력
cv2.imshow('Original Grayscale Image', image)
cv2.imshow('Contrast Adjusted Image', dst)

# 히스토그램 비교
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

hist_orig = cv2.calcHist([image], [0], None, [256], [0, 256])
axes[0].plot(hist_orig, color='blue')
axes[0].set_title('Histogram of Original Image')
axes[0].set_xlabel('Pixel Intensity')
axes[0].set_ylabel('Frequency')
axes[0].set_xlim([0, 256])

hist_dst = cv2.calcHist([dst], [0], None, [256], [0, 256])
axes[1].plot(hist_dst, color='red')
axes[1].set_title('Histogram of Contrast Adjusted Image')
axes[1].set_xlabel('Pixel Intensity')
axes[1].set_ylabel('Frequency')
axes[1].set_xlim([0, 256])

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
