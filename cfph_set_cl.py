import json
import sys
import openpyxl

def setChecklist(fileRoute, checklist):
    # 엑셀 파일 열기
    workbook = openpyxl.load_workbook(fileRoute, data_only=False)
    worksheet = workbook.active

    # 엑셀 1행 파싱
    header = [cell.value for cell in worksheet[1]]
    noIndex = header.index("No")
    resultIndex = header.index("Result")

    # 각 체크리스트 아이템 처리
    for item in checklist:
        targetRow = None
        # 대상 행 찾기 (3행부터 시작)
        for row in worksheet.iter_rows(min_row=3):
            if str(item["No"]) == str(row[noIndex].row - 2):
                targetRow = row
                break   
        
        if targetRow is None:
            print(f"오류: No {item['No']}에 해당하는 행을 찾을 수 없습니다.")
            continue

        # 값 업데이트
        targetRow[resultIndex].value = item['Result']

    # 저장
    workbook.save(fileRoute)

def main():
    checklistFileRoute = sys.argv[1]
    checklist = json.loads(sys.argv[2])
    # checklistFileRoute = "D:\Portpolio\CFPH_Test.sikuli\cfph_cl.xlsx"

    setChecklist(checklistFileRoute, checklist)
    print("Update Checklist")

if __name__ == '__main__':
    main()