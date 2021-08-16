
for reportCnt in range(1,51):
    fileName = str(reportCnt) + "주차.txt"
    print(fileName)
    reportFile = open(fileName, "w", encoding="utf8")
    reportFile.write("- " + str(reportCnt) + " 주차 주간보고 -\n")
    reportFile.write("부서 : \n")
    reportFile.write("이름 : \n")
    reportFile.write("업무요약 : \n")
    reportFile.close()
