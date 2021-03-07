from tkinter import *


root1 = Tk()
root1.title("Test")
root1.geometry("400x300")

photo1 = PhotoImage(file = "GUI/circle.png")        # 포토1 이미지 지정
photo2 = PhotoImage(file = "GUI/cross.png")         # 포토2 이미지 지정
photoCtl = photo1       # 포토1 이미지를 "hptoCtl" 변수에 할당(?)
btnCnt = 1      # 버튼의 상태 체크를 위한 컨트롤 변수


def btncng():
    global btnCnt
    if btnCnt == 1:
        btn1.config(image = photo2)
        btnCnt = 2
    else:
        btn1.config(image = photo1)
        btnCnt = 1

    label3.config(text=btnCnt)
btn1 = Button(root1, image=photo1, width = 60, height = 60, command = btncng)       # 버튼1에 "이미지"와 "command" 지정
btn1.pack() 
label3 = Label(root1, text = btnCnt)
label3.pack()   
root1.mainloop()