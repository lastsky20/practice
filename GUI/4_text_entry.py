from tkinter import *


root = Tk()
root.title("GUI_Practice")
root.geometry("640x480")

txt = Text(root, width = 30, height = 5)
txt.pack()

txt.insert(END, "텍스트 입력 창")

e = Entry(root, width = 30)
e.pack()

e.insert(0, "엔트리 입력 창")

def btnCmd1() : 
    print(txt.get("1.0", END))      # 1번째 라인, 0번 칼럼부터 끝까지 가져온다
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)


btn1 = Button(root, text = "버튼1", command = btnCmd1)
btn1.pack()

root.mainloop()