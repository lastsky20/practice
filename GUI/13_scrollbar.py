import tkinter.messagebox as msgbox 
from tkinter import *

root = Tk()
root.title("GUI_Practice")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side = "right", fill = "y")      # scrollbar 정의 및 pack

listbox = Listbox(frame, selectmode = "extended", height = 10, yscrollcommand = scrollbar.set)  # scrollbar.set
for i in range(1, 31) :
    listbox.insert(END, str(i) + "일")
listbox.pack(side = "left")

scrollbar.config(command = listbox.yview)   # listbox.yview

root.mainloop() 