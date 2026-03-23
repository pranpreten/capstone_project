import cv2
import matplotlib.pyplot as plt

# Lenna 이미지를 BGR로 읽기
image = cv2.imread('images/Lenna.png')

if image is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
else:
    # 원본 이미지 출력
    cv2.imshow('BGR Image', image)

    # BGR 각 채널별 히스토그램 계산 및 출력
    colors = ('b', 'g', 'r')
    labels = ('Blue', 'Green', 'Red')

    plt.figure()
    plt.title("BGR Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")

    for i, (col, label) in enumerate(zip(colors, labels)):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col, label=label)

    plt.xlim([0, 256])
    plt.legend()
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
