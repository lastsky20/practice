

import tkinter.messagebox as msgbox 
from tkinter import *

root = Tk()
root.title("GUI_Practice")
root.geometry("640x480")

Label(root, text = "Menu").pack(side = "top")
Button(root, text = "Order").pack(side = "bottom")

# menu frame
frame_burger = Frame(root, relief = "solid", bd = 1)
frame_burger.pack(side = "left", fill = "both", expand = True)

Button(frame_burger, text = "Hamburger").pack()
Button(frame_burger, text = "burger2").pack()
Button(frame_burger, text = "Burger3").pack()

# Drink frame
frame_drink = LabelFrame(root, text = "Drink")
frame_drink.pack(side = "right", fill = "both", expand = True)
Button(frame_drink, text = "cola").pack()
Button(frame_drink, text = "sidar").pack()
Button(frame_drink, text = "fanta").pack()

root.mainloop() 