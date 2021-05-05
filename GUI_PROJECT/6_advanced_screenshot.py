import time  
import keyboard 
from PIL import ImageGrab


def screenshot():
    #2021년 5월 2일 8시 33분 30초 -> _20210502_083330
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("F9", screenshot)

keyboard.wait("esc", quit)
