import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI_Practice")
root.geometry("640x480")


values = [str(i) + " 일" for i in range(1, 32)]     # 1~31 까지의 숫자를 values 값에 저장(+일)
combobox = ttk.Combobox(root, height = 5, values = values)
combobox.pack()
combobox.set("카드 결제일")     # 기본값 설정


ro_combobox = ttk.Combobox(root, height = 10, values = values, state="readonly")    #읽기 전용으로 state 설정
ro_combobox.current(0)
ro_combobox.pack()
# ro_combobox.set("카드 결제일")     # 기본값 설정

def btnCmd1() : 
    print(combobox.get())      # 선택된 값 출력
    print(ro_combobox.get())

btn1 = Button(root, text = "선택", command = btnCmd1)
btn1.pack()

root.mainloop() 