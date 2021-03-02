import ctypes
import time
from tkinter import *

"""
MB_OK = 0x0
MB_OKCXL = 0x01
MB_YESNOCXL = 0x03
MB_YESNO = 0x04
MB_HELP = 0x4000
ICON_EXLAIM=0x30
ICON_INFO = 0x40
ICON_STOP = 0x10
import math
import time

for i in range(200):
    x = int(500 + math.cos(i / 5) * i)
    y = int(500 + math.sin(i / 5) * i)
    ctypes.windll.user32.SetCursorPos(x, y)
    time.sleep(0.05)
result = ctypes.windll.user32.MessageBoxA(0, "Your text?", "Your title", MB_HELP| MB_YESNO | ICON_STOP)
"""


# TODO Make this an external admin process
class BlackWindow:
    def __init__(self, time):
        self.root = Tk()
        self.root.title("app")

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.attributes('-fullscreen', True)

        self.root.configure(background='black')
        self.root.lift()
        self.root.after(time * 1000, self.root.quit)
        self.root.mainloop()

    def on_closing(self):
        self.root.destroy()


def block_input(time):
    ctypes.windll.user32.BlockInput(ctypes.c_bool(True))
    time.sleep(time)
    ctypes.windll.user32.BlockInput(ctypes.c_bool(False))
