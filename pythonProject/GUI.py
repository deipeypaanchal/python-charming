import tkinter

class GUISec3:
    def __init__(self):
        self.mainwindow = tkinter.Tk()

        # self.label = tkinter.Label(self.mainwindow, text = "Main Window Label.")
        # self.label.pack(side = "left")

        self.topframe = tkinter.Frame(self.mainwindow)
        self.bottomframe = tkinter.Frame(self.mainwindow)

        self.tflabel = tkinter.Label(self.topframe, text = "Top Frame Label", borderwidth = 2, relief = "groove")
        self.bflabel = tkinter.Label(self.bottomframe, text = "Top Bottom Label", borderwidth = 2, relief = "groove")

        self.tflabel.pack(side = "top")
        self.bflabel.pack(side = "bottom")

        self.topframe.pack(side = "top")
        self.bottomframe.pack(side = "bottom")


        tkinter.mainloop()

myGUI = GUISec3()

