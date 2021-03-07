from tkinter import *

root = Tk()
root.title("GUI_Practice")
root.geometry("640x480")

burger_var  = IntVar()
drink_var = StringVar()

Label(root, text = "버거를 선택 하세요").pack()
btn_burger = Radiobutton(root, text = "햄버거", value = 1, variable = burger_var)
btn_burger.select()
btn_burger2 = Radiobutton(root, text = "치즈버거", value = 2, variable = burger_var)
btn_burger3 = Radiobutton(root, text = "새우버거", value = 3, variable = burger_var)

btn_burger.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text = "음료를 선택 하세요.").pack()
btn_drink = Radiobutton(root, text = "콜라", value = "콜라", variable = drink_var)

btn_drink2 = Radiobutton(root, text = "사이다", value = "사이다", variable = drink_var)
btn_drink.pack()
btn_drink2.pack()

def btnCmd1() : 
    print("선택된 햄버거 : ", burger_var.get())
    print("선택된 음료 : ", drink_var.get())
    # try :
    
    # except :
        
btn1 = Button(root, text = "버튼1", command = btnCmd1)
btn1.pack()

root.mainloop()