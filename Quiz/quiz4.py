from random import *

quiz_list = ["orange", "apple", "banana"]       # 퀴즈에 사용될 단어 리스트
quizNum = int(random() * 3)                     # 퀴즈에 사용될 단어중 몇번째 것을 사용할지 결정하기 위한 1자리 정수
print("Question: " + quiz_list[quizNum])        # 퀴즈에 사용될 1개의 단어를 미리 출력함
answerList = []                                 # 사용자 입력값을 저장할 리스트
finalString = ""                                # 사용자가 입력한 모든 최종값을 저장할 변수
answer = ""                                     # 사용자가 입력할 문자 변수
checkTrue = 4                                   # "Correct", "Wrong" 을 판별하기 위한 변수

for i in range(0, len(quiz_list[quizNum])):     # 사용자 입력값을 저장할 리스트에 사용될 단어의 길이만큼 "_"를 입력
    answerList.insert(i,"_")

while True:
    for a in range(0, len(quiz_list[quizNum])):  # 사용자 입력값을 리스트와 비교, 같은문자를 찾으면 / 대입
        if quiz_list[quizNum][a] == answer:
            if answerList[a] == "_":
                answerList[a] = answer
            checkTrue = 1
        elif checkTrue == 3:
            checkTrue = 2
        
        finalString += answerList[a]
    
    if checkTrue == 1:
            print("Correct!")
    elif checkTrue == 2:
            print("Wrong!")

    checkTrue = 3
    # checkFalse = 3

    print(f"finalString => {finalString}")
    
    for a in range(0, len(quiz_list[quizNum])):  #사용자 입력 문자의 누계를 언더바와 함께 출력
        if a  == len(quiz_list[quizNum]) - 1:
            print(f"{answerList[a]}\n",end="")
            break
        else:
            print(f"{answerList[a]}",end=" ")

    if str(quiz_list[quizNum]) == finalString:      # 정답을 맞추면 "while" 문을 벗어남
        print(f"정답 => {finalString}")
        break
    else:   # 정답이 아닐경우 "finalString" 값을 초기화
        finalString = ""

    answer = input("Input letter > ") #사용자 입력값 / 입력






