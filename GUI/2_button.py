from tkinter import *


root1 = Tk()                                                    # 윈도우 객체 생성

root1.title("Test1")
root1.geometry("600x400")

btn1 = Button(root1, width = 5, height = 2, text = "test1")   # 버튼 생성, 버튼의 크기 지정, 고정크기
btn1.pack()     # 버튼 활성화


btn2 = Button(root1, padx = 5, pady = 10 , text = "Button2")    # 버튼 생성, 버튼의 텍스트 여백 지정, 가변크기
btn2.pack()     # 버튼 활성화

btn4 = Button(root1, fg = "red", bg = "yellow", padx = 5, pady = 2, text = "컬러버튼")  # 버튼의 색상을 지정
btn4.pack()

photo1 = PhotoImage(file="GUI/circle.png")
btn5 = Button(root1, image = photo1)
btn5.pack()


def btncmd():
    root2 = Tk()                            # 윈도우 객체 생성
    root2.title("command btn window")       # 타이틀 지정
    root2.geometry("400x400")               # 윈도우 사이즈 지정
    root2.resizable(False, False)           # 윈도우 크기 조정 false
    root2.pack()                            # 윈도우 활성화
    root2.mainloop()                        # 사용자 종료시까지 활성화
    

btn3 = Button(root1, text="커맨드 버튼", command=btncmd)        # 버튼의 커맨드 지정, "command" 항목에 정의함수 지정
btn3.pack() # 버튼 활성화

root1.mainloop()
