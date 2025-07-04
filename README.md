# Test_Automation

<img src="https://github.com/user-attachments/assets/1036df74-06e2-429d-9518-809ba899e9ee" width="400" alt="제목-없는-동영상-Clipchamp로-제작"/> </br>


CrossFire PH의 Store/Weapon/Melee 카테고리 항목의 UI가 정상출력되고 있는지 자동화 테스트를 하는 프로젝트입니다. <br/>
SikuliX와 Tesseract OCR을 이용하며, 각 관련 정보는 아래의 링크를 확인해주세요! <br/>

**SikuliX GitHub :** https://github.com/RaiMan/SikuliX1 <br/>
**Google Tesseract OCR GitHub :** https://github.com/tesseract-ocr/tesseract <br/>
<br/>
<br/>
## 시작
먼저, 동작환경은 아래와 같습니다. <br/>
<br/>
**OS :** Window 11 <br/>
**해상도 :** 2560 X 1440, 스케일 100% <br/>
<br/>

SikuliX를 실행하기 위해선 Java JDK 8 이상이 필요합니다. <br/>
**Java JDK Download :** https://www.oracle.com/java/technologies/downloads/ <br/>
<br/>

Tesseract OCR을 사용하기 위해 Python이 필요합니다. <br/>
**Python Download :** https://www.python.org/downloads/ <br/>
<br/>

Java와 Python이 설치되어있는지 cmd를 통해 확인합니다. <br/>
```
java --version
python --version
```
프로젝트에 사용된 pip은 다음과 같습니다.<br/>
```
pip install openpyxl
pip install pytesseract
pip install json
pip install cv2
```

이제 CrossFire PH -> SikuliX 순으로 실행하고, 다운/클론한 코드를 실행하고자 하는 .sikuli 폴더에 추가하고 테스트를 진행합니다. <br/>

## 라이센스
'누구나 사용'할 수 있고 또 MIT 라이센스 하에서 '누구나 재배포' 하실 수 있습니다.
