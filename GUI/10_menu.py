
from tkinter import *

root = Tk()
root.title("GUI_Practice")
root.geometry("640x480")

def btnCmd2() :
    pass

def create_new_file() : 
    print("새 파일을 만듭니다.")

menu = Menu(root)   # 1

# 파일 메뉴
menu_file = Menu(menu, tearoff = 0)  # 2

menu_file.add_command(label = "New File", command=create_new_file)  # 3
menu_file.add_command(label = "New Window")
menu_file.add_separator()   # 3
menu_file.add_command(label = "Open file...")
menu_file.add_separator()
menu_file.add_command(label = "Save All", state = DISABLED)     # 메뉴 비활성화
menu.add_cascade(label = "File", menu=menu_file)    # 4

menu_file.add_separator()
menu_file.add_command(label = "Exit", command = root.quit)

# Edit 메뉴
menu.add_cascade(label = "Edit")


# Radio 버튼
menu_lang = Menu(menu, tearoff = 0)
menu_lang.add_radiobutton(label = "python")
menu_lang.add_radiobutton(label = "JAVA")
menu_lang.add_radiobutton(label = "C++")
menu.add_cascade(label = "Language", menu=menu_lang)

# checkBox
menu_view = Menu(menu, tearoff = 0)
menu_view.add_checkbutton(label = "Show Minimap")
menu.add_cascade(label = "View", menu = menu_view)


root.config(menu = menu)    # 5

root.mainloop() 