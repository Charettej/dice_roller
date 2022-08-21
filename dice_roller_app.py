from random import randint
import statistics
from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.label1 = Label(window, text= 'Enter number of sides:', font = ('courier', 10))
        self.label2 = Label(window, text= 'Enter number of dice:', font = ('courier', 10))
        self.label3 = Label(window, text= 'Result:', font = ('courier', 10))
        self.label4 = Label(window, text= 'DICE ROLLER', font= ('courier', 20))
        self.t1 = Entry() #input for dsides
        self.t2 = Entry() #input for dnum
        self.t3 = Entry() #output for result
        self.button1 = Button(win, text='Roll Dice')
        self.label1.place(x=100, y=100)
        self.t1.place(x=300, y=100)
        self.b1 = Button(win, text='Roll', font=("Courier", 16), command=self.roll)
        self.b1.place(x=300, y=210)
        self.b1.config(height=1, width=8)
        self.label2.place(x=100, y=160)
        self.t2.place(x=300, y=160)
        self.label4.place(x=100, y=35)
        self.label3.place(x=100, y=280)
        self.t3.place(x=300, y=280)

    def roll(self):
        self.t3.delete(0, 'end')
        dsides = int(self.t1.get())
        dnum = int(self.t2.get())
        if dsides > 3 and dnum > 0:
            for i in range(dnum):
                self.t3.insert(END, str(randint(1, dsides)) + ', ')
        else:
            self.t3.insert(END, str("Invalid Input"))

window = Tk()
mywin = MyWindow(window)
window.title('Dice Roller')
window.geometry("500x400+50+50")
window['background'] = '#F5E4CE'
window.mainloop()
