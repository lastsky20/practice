from tkinter import *

root = Tk()
root.title("GUI_Practice")
root.geometry("640x480")


chkvar = IntVar()
chkvar2 = IntVar()

chkbox1 = Checkbutton(root, text = "오늘 하루 보지 않기", variable = chkvar)
chkbox2 = Checkbutton(root, text = "일주일 동안 보지 않기", variable = chkvar2)
chkbox1.pack()
chkbox2.pack()

def btnCmd1() : 
    global chkvar
    print("체크박스 1번 값 : ",chkvar.get())
    print("체크박스 1번 값 : ",chkvar2.get())
    # try :
        

    # except :
        


btn1 = Button(root, text = "버튼1", command = btnCmd1)
btn1.pack()

root.mainloop()