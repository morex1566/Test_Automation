import re
import subprocess
import sys
import os
import json

Settings.ImageQuality = 1.0
Settings.OcrLanguage = "eng"
Settings.OcrTextSearch = True
Settings.OcrTextRead = True

reload(sys)
sys.setdefaultencoding('utf-8')

capturedImgPath = getBundlePath()
capturedImgName = 'testing.png'

tesseractScriptPath = getBundlePath()
tesseractScriptName = 'cfph_tesseract.py'

clFilePath = getBundlePath()
clFileName = 'cfph_cl.xlsx'

getCLScriptPath = getBundlePath()
getCLScriptName = 'cfph_get_cl.py'

setCLScriptPath = getBundlePath()
setCLScriptName = 'cfph_set_cl.py'

regions = []

# 상점 아이템 구매 위치
regions.append(Region(649,291,388,158))
regions.append(Region(1046,286,392,163))
regions.append(Region(1443,288,390,160))
regions.append(Region(650,449,387,160))
regions.append(Region(1047,451,388,158))
regions.append(Region(1446,450,389,160))
regions.append(Region(650,615,386,159))
regions.append(Region(1049,613,387,159))
regions.append(Region(1445,613,390,160))
regions.append(Region(650,777,387,155))
regions.append(Region(1043,777,393,157))
regions.append(Region(1444,772,389,163))

#페이지 이동 위치
pageDown = Region(Region(1842,902,31,36))

#이미지 캡처
def captureImg(region, savePath, saveName):
    capturedImg = Screen().capture(region)
    capturedImg.save(capturedImgPath, capturedImgName)
    return capturedImg

# OCR 텍스트 추출
def getTextFromCaptureImg():
    python = "python"
    tesseractScriptRoute = os.path.join(tesseractScriptPath, tesseractScriptName)
    capturedImgRoute = os.path.join(capturedImgPath, capturedImgName)

    process = subprocess.Popen([python, tesseractScriptRoute, capturedImgRoute],
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE, 
                                universal_newlines=True)

    stdout, stderr = process.communicate()
    if stdout:
        return json.loads(stdout)
    elif stderr:
        return stderr
    else:
        return ""
    
# 체크리스트 가져오기
def getChecklist():
    python = "python"
    getChecklistScriptRoute = os.path.join(getCLScriptPath, getCLScriptName)
    checklistFileRoute = os.path.join(clFilePath, clFileName)
    
    # 체크리스트 가져오는 스크립트 별도 실행
    process = subprocess.Popen([python, getChecklistScriptRoute, checklistFileRoute],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                universal_newlines=True)
    
    stdout, stderr = process.communicate()
    if stdout:
        return json.loads(stdout)
    elif stderr:
        return stderr
    else:
        return ""
    
# 체크리스트 수정
def setChecklist(checklist):
    python = "python"
    setChecklistScriptRoute = os.path.join(setCLScriptPath, setCLScriptName)
    checklistFileRoute = os.path.join(clFilePath, clFileName)

    process = subprocess.Popen([python, setChecklistScriptRoute, checklistFileRoute, json.dumps(checklist, ensure_ascii=False, indent=2)],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                universal_newlines=True)
    
    stdout, stderr = process.communicate()
    if stdout:
        print(stdout)
        return stdout
    elif stderr:
        return stderr
    else:
        return ""

# 자동화 테스트 시작
# 목표 : 상점에 근접 무기 등록됨 확인하기
def test(checklist): 
    
    i = 0
    maxCount = len(checklist) * len(regions)
    count = 0
    found = False
    while i < len(checklist):
        
        # 상점의 무기 구매 항목 순회
        testText = re.sub(r'\s+', '', checklist[i]['Depth 4'])
        print("target : " + testText)
        for region in regions:
            captureImg(region, capturedImgPath, capturedImgName)
            region.highlight(0.1)
            
            # 무기 구매 항목 이미지의 텍스트 공백없는 한줄로 전환
            extractTexts = ''.join(text.strip() for text in getTextFromCaptureImg())
            fullText = re.sub(r'\s+', '', extractTexts)
            print("curr : " + fullText)
            # 찾기 성공
            if testText in fullText:
                found = True
                count = 0
                break
            else:
            # 찾기 실패
                found = False
                count += 1

        # 1. 못찾으면 다음 페이지에서 찾기
        # 2. 모든 페이지에 없으면 테스트 오류 기록
        # 3. 찾으면 테스트 성공 기록
        if found == False and count < maxCount:
            pageDown.click()
        elif found == False and count >= maxCount:
            print("Not Found " + checklist[i]['Depth 4'])
            checklist[i]['Result'] = 'Fail'
            i += 1
            count = 0
            found = False
        elif found == True:
            checklist[i]['Result'] = 'Pass'
            print("Found " + checklist[i]['Depth 4'] + " in region")
            i += 1
            count = 0
            found = False
        
    return checklist

def main():
    checklist = getChecklist()
    checklist = test(checklist)
    print(checklist)
    setChecklist(checklist)
    
if __name__ == '__main__':
    main()