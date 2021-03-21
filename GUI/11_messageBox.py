
import tkinter.messagebox as msgbox 
from tkinter import *

root = Tk()
root.title("GUI_Practice")
root.geometry("640x480")


def info() : 
    msgbox.showinfo("알림", "예매확인")
    print("예매 확인")

def warn() :
    msgbox.showwarning("경고", "경고 입니다")
 
def error() :
    msgbox.showerror("에러", "에러 입니다")


def okcancel() :
    response = msgbox.askokcancel("확인 / 취소", "확인, 취소")
    print(response)
def rtcancel() :
    msgbox.askretrycancel("재시도 /취소", "재시도, 취소")

def yesno() :
    response = msgbox.askyesno("예 / 아니오", "예, 아니오")
    print(response)

def yesnocancel():
    response = msgbox.askyesnocancel("예, 아니오, 취소","예, 아니오, 취소")
    print(response)

    if response == 1 : 
        print("예")
    elif response == 0 :
        print("아니오")
    else :
        print("취소")


Button(root, command = info, text = "알림1").grid(row = 2, column = 2)
# Button(root, command = warn, text = "경고").pack()
# Button(root, command = error, text = "에러").pack()
# Button(root, command = okcancel, text = "예 / 아니오").pack()
# Button(root, command = rtcancel, text = "재시도 / 아니오").pack()
# Button(root, command = yesno, text = "예 / 아니오").pack()
btn1 = Button(root, command = yesnocancel, text = "예, 아니오, 취소", width = 15)
btn1.grid(row = 2, column = 1)
# pack() 과 grid() 는 같이 쓸수 없다.
root.mainloop() 