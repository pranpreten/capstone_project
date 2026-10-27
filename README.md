# OpenCV 영상처리 기초 실습

이미지·동영상·카메라 입력을 다루고 기본 영상처리 연산을 확인하는 OpenCV 실습 모음이다. 각 파일을 독립적으로 실행하면서 입력과 처리 결과를 비교하는 형태로 구성되어 있다.

## 실습 내용

- 이미지 읽기와 창 표시
- 동영상 재생 및 웹캠 입력
- 채널 분리와 HSV 색공간 변환
- 히스토그램 평활화
- 평균·샤프닝·라플라시안 필터 적용

## 대표 파일

| 파일 | 내용 |
|---|---|
| `week3/ex1_opencv_readImg.py` | 이미지 읽기 및 표시 |
| `week3/ex2_opencv_readVideo.py` | 동영상 프레임 읽기 |
| `week3/ex3_opencv_readCam.py` | 카메라 스트림 표시 |
| `week3/ex4_opencv_split.py` | 영상 채널 분리 |
| `week3/ex5_opencv_cvtColor_HSV.py` | HSV 변환 |
| `week3/ex10_opencv_equalizeHist.py` | 히스토그램 평활화 |
| `week3/ex13_opencv_filtering.py` | 공간 필터별 결과 비교 |

## 실행 방법

GUI 창을 지원하는 `opencv-python`과 NumPy를 사용한다. `opencv-python-headless`만 설치된 환경에서는 `imshow` 창을 사용할 수 없다.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install opencv-python numpy
.\.venv\Scripts\python.exe week3/ex3_opencv_readCam.py
```

카메라 예제는 연결된 웹캠과 카메라 접근 권한이 필요하며 `q` 키로 종료한다.

## 이미지·동영상 준비

이미지 읽기 예제는 현재 작업 폴더의 `images/Lenna.png`를 사용한다. 사용할 이미지를 이 경로에 두거나 코드의 파일 경로를 실제 이미지로 바꾼다. 다른 예제도 `imread`·`VideoCapture`에 지정된 입력 경로를 확인한 뒤 실행한다.

```powershell
.\.venv\Scripts\python.exe week3/ex1_opencv_readImg.py
.\.venv\Scripts\python.exe week3/ex13_opencv_filtering.py
```

## 결과와 학습 범위

원본과 처리 결과를 별도 창에서 비교한다. 필터에 따라 평활화·경계 강조·세부 정보 변화가 어떻게 달라지는지 관찰할 수 있다. 외부 학습 데이터나 학습 모델을 사용하는 프로젝트가 아니라 영상처리 연산을 익히기 위한 실습이다. 모든 파일을 실행하는 통합 메뉴나 결과 자동 저장 기능은 별도로 구성되어 있지 않다.

---

[GitHub 저장소](https://github.com/pranpreten/capstone_project) · [문서 작성 기준 코드](https://github.com/pranpreten/capstone_project/tree/5f3dc483f0482ba1757e2e01669fa435f1ead4a7)
