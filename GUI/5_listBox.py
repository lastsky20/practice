from tkinter import *

root = Tk()
root.title("GUI_Practice")
root.geometry("640x480")

# listbox = Listbox(root, selectmode = "extended", height = 0)
# listbox.insert(END, "Apple")
# listbox.insert(END, "Orange")
# listbox.insert(END, "Banana")
# listbox.insert(END, "Kiwi")
# listbox.insert(END, "WaterMelon")
# listbox.pack()


opt_list = ["Apple", "Orange", "Banana", "Kiwi", "WaterMelon"]
listbox = Listbox(root, selectmode = "extended", height = 0, cursor = "top_left_corner")

for opt in opt_list : 
    listbox.insert(END, opt)
listbox.pack()


def btnCmd1() : 
    try :
        global listNum
        listNum = listbox.curselection()
        # print("선택된 항목 : ",listbox.get(listNum))      # 에러
        # print("선택된 항목 {0}".format(listNum))          # 에러
        print("index : ",listbox.curselection())
        
        for i in listNum :      # 선택된 리스트의 값을 한줄씩 출력
            print("선택된 항목 : ", listbox.get(i))

    except :
        print("선택된 값이 없습니다.")


btn1 = Button(root, text = "버튼1", command = btnCmd1)
btn1.pack()

root.mainloop()