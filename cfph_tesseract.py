import cfph_utls
import json
import sys
import cv2
import pytesseract

def extractText():
    # 명령줄 인자로 이미지 경로 받기
    imgPath = sys.argv[1]

    # 이미지 읽기
    img = cv2.imread(imgPath)
    if img is None:
        print("Error: Could not load image at", imgPath)
        sys.exit(1)

    # 전치리 과정
    # 1. 그레이스케일
    # 2. 이진화
    # 3. 업스케일
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    postProcessedImg = cv2.resize(binary_image, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

    # 이미지 텍스트화
    text = pytesseract.image_to_string(postProcessedImg, lang='eng')
    
    print(json.dumps(text, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    extractText()
