import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI_Practice")
root.geometry("640x480")

# pvar = ttk.Progressbar(root, maximum = 100, mode="indeterminate")
# pvar2 = ttk.Progressbar(root, maximum = 100, mode="determinate")
# pvar.pack()
# pvar2.pack()
# pvar.start(10)
# pvar2.start(10)


p_var2 = DoubleVar()
pvar = ttk.Progressbar(root, maximum = 100, length = 150, variable = p_var2)    # 최대값 100, 길이 150, variable = 변수
pvar.pack()

# def btnCmd1() : 
    # pvar.stop() 


def btnCmd2() :
    for i in range(101) :
        time.sleep(0.01)
        p_var2.set(i)
        pvar.update() 
        print(p_var2.get())
# btn1 = Button(root, text = "정지", command = btnCmd1)
# btn1.pack()
btn2 = Button(root, text = "시작", command = btnCmd2)
btn2.pack()

root.mainloop() 