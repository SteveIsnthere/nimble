from tkinter import *


class UI:
    def __init__(self):
        body = Tk()
        var = StringVar()
        var.set("world")
        label1 = Label(body, text="hello")
        label1.pack()
        label2 = Label(body, textvariable=var)
        label2.pack()

        def on_click():
            var.set("shit")

        button = Button(body, text="button", command=on_click)

        button.pack()
        body.mainloop()
