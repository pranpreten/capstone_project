import cv2
import matplotlib.pyplot as plt

# 이미지를 그레이스케일로 읽기
image = cv2.imread('images/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
    exit()

# 히스토그램 평활화 (균등화)
dst = cv2.equalizeHist(image)

# 원본 및 결과 이미지 출력
cv2.imshow('Original Grayscale Image', image)
cv2.imshow('Normalized Image', dst)

# 히스토그램 비교
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

hist_orig = cv2.calcHist([image], [0], None, [256], [0, 256])
axes[0].plot(hist_orig, color='blue')
axes[0].set_title('Original Image Histogram')
axes[0].set_xlabel('Pixel Intensity')
axes[0].set_ylabel('Frequency')
axes[0].set_xlim([0, 256])

hist_dst = cv2.calcHist([dst], [0], None, [256], [0, 256])
axes[1].plot(hist_dst, color='red')
axes[1].set_title('Normalized Image Histogram')
axes[1].set_xlabel('Pixel Intensity')
axes[1].set_ylabel('Frequency')
axes[1].set_xlim([0, 256])

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
