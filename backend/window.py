import tkinter
from tkinter import *


class BlackWindow:
    def __init__(self, time):
        self.time = int(time)
        self.root = Tk()
        self.root.title("app")
        # da mettere al centro
        self.label = Label(self.root,text="Counter", font=('Helvetica', 48), fg='red', anchor=CENTER)
        self.label.place(relx=0.5,
                         rely=0.5,
                         anchor='center')
        self.label.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.attributes('-fullscreen', True)

        self.root.configure(background='black')
        self.root.lift()
        self.countdown()
        self.root.after(self.time * 1000, self.root.quit)
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
            self.time -= 1
            self.root.after(1000, self.countdown)


if __name__ == '__main__':
    c = BlackWindow(50)
    pass
