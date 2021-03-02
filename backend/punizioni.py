import ctypes
import time
import tkinter
from tkinter import *
import random

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


def select_punizione():
    punzioni = [BlackWindow]
    punizione = punzioni[random.randint(0, len(punzioni)-1)]
    time_execution = round(random.SystemRandom().uniform(1, 5),2)
    return punizione, time_execution


# TODO Make this an external admin process
class BlackWindow:
    def __init__(self, time):
        self.time=int(time) -1
        self.root = Tk()
        self.root.title("app")
        self.label = Label(text="Counter", font=('Helvetica', 48), fg='red')
        self.label.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        #self.root.attributes('-fullscreen', True)

        self.root.configure(background='black')
        self.root.lift()
        self.countdown()
        self.root.after(self.time +1 * 1000, self.root.quit)
        self.root.mainloop()

    def on_closing(self):
        self.root.destroy()
    def close(self):
        self.root.destroy()
    def countdown(self):
        # change text in label
        self.label.configure(text=self.time)

        if self.time > 0:
            # call countdown again after 1000ms (1s)
            self.time -=1
            self.root.after(1000, self.time)

def block_input(time):
    ctypes.windll.user32.BlockInput(ctypes.c_bool(True))
    time.sleep(time)
    ctypes.windll.user32.BlockInput(ctypes.c_bool(False))
