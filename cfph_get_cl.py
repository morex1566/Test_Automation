import sys
import openpyxl
import json

def getChecklist(fileRoute):
    # 엑셀 파일 열기
    workbook = openpyxl.load_workbook(fileRoute, data_only=True)
    worksheet = workbook.active

    # 엑셀 1행 파싱
    header = [cell.value for cell in worksheet[1]]
    noIndex = header.index("No")
    depth1Index = header.index("Depth 1")
    depth2Index = header.index("Depth 2")
    depth3Index = header.index("Depth 3")
    depth4Index = header.index("Depth 4")
    checkpointIndex = header.index("Checkpoint")
    resultIndex = header.index("Result")

    # 출력할 데이터
    checklist = []
    checklistItem = {
        "No": None,
        "Depth 1": None,
        "Depth 2": None,
        "Depth 3": None,
        "Depth 4": None,
        "Checkpoint": None,
        "Result": None
    }

    # 엑셀 ~N행까지 파싱
    no = 1
    for row in worksheet.iter_rows(min_row=3, values_only=True):
        depth1 = row[depth1Index]
        depth2 = row[depth2Index]
        depth3 = row[depth3Index]
        depth4 = row[depth4Index]
        checkpoint = row[checkpointIndex]
        result = row[resultIndex]

        # 병합 셀 처리: 값이 있으면 갱신, 없으면 이전 값 유지
        if depth1 is not None:
            checklistItem["Depth 1"] = depth1
        if depth2 is not None:
            checklistItem["Depth 2"] = depth2
        if depth3 is not None:
            checklistItem["Depth 3"] = depth3
        if depth4 is not None:
            checklistItem["Depth 4"] = depth4
        if checkpoint is not None:
            checklistItem["Checkpoint"] = checkpoint
        if result is not None:
            checklistItem["Result"] = result

        checklist.append({
            "No": no,
            "Depth 1": checklistItem["Depth 1"],
            "Depth 2": checklistItem["Depth 2"],
            "Depth 3": checklistItem["Depth 3"],
            "Depth 4": checklistItem["Depth 4"],
            "Checkpoint": checklistItem["Checkpoint"],
            "Result": checklistItem["Result"]
        })

        no += 1

    return checklist

def main():
    # 테스트용
    # checklistFileRoute = "D:\Portpolio\CFPH_Test.sikuli\cfph_cl.xlsx"
    checklistFileRoute = sys.argv[1]

    checklist = getChecklist(checklistFileRoute)
    print(json.dumps(checklist, ensure_ascii=False, indent=2))
    
if __name__ == '__main__':
    main()