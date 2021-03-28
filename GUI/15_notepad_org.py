import os
from tkinter import *

root = Tk()
root.title("제목없음")              # 타이틀(제목)
root.geometry("600x600")       # 윈도우의 크기
# 크기 변경 가능하도록 설정시 불필요
# root.resizable(True, True)     # 버튼의 크기 조절, x값과 y값을 true, false 로 지정하여 허용여부 지정

def open_file():
    if os.path.isfile("mynote.txt"): 
        with open("mynote.txt", "r", encoding = "utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())

    print("열기")

def save_file():
    with open("mynote.txt", "w", encoding = "utf8") as file:
        file.write(txt.get("1.0", END))   # 
    
    print("저장")    

#파일(열기, 저장, 끝내기), 편집, 서식, 보기, 도움말
menu = Menu(root)

menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = "열기", command = open_file)
menu_file.add_command(label = "저장", command = save_file)
menu_file.add_separator()
menu_file.add_command(label = "종료", command = root.quit)
menu.add_cascade(label = "파일(F)", menu = menu_file)

menu_edit = Menu(menu, tearoff = 0)
menu.add_cascade(label="편집(E)", menu = menu_edit)

menu_form = Menu(menu, tearoff = 0)
menu.add_cascade(label="서식(O)", menu = menu_form)

menu_view = Menu(menu, tearoff = 0)
menu.add_cascade(label="보기(V)", menu = menu_view)

menu_help = Menu(menu, tearoff = 0)
menu.add_cascade(label="도움말(H)", menu = menu_help)

root.config(menu = menu)


# Scroll Bar
scrollbar = Scrollbar(root)
scrollbar.pack(side = "right", fill = "y")      # scrollbar 정의 및 pack


# Text entry
txt = Text(root, yscrollcommand = scrollbar.set)
txt.pack(side = "left", fill = "both", expand = True)

scrollbar.config(command = txt.yview)




root.mainloop()
