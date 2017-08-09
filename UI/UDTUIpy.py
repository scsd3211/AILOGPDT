import tkinter as tk
from tkinter import *
from UDTLOGIC import showme
class Application(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.Voicetext = ["UDT", "Personal or Group", "Source Address", "Target Address", "Encrypt or not", "Others",
                          "NO way"]
        self.Labelm = [1, 2, 3, 4, 5, 6, 7];
        self.Encrym = [1, 2, 3, 4, 5, 6, 7];
        self.root = master
        self.pack()
        #self.createWidgets()
        self.packLabel()
        self.UDTCustomeLive = True
        self.ifRun = True
        showme.showme()
        #self.createWidgets()



    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red")
        self.QUIT.pack(side="bottom")
    def packLabel(self):
        #self.Label[0] = tk.Label()
        for tempi in range(7):
            #self.Labelm[tempi] = tk.Label(self.root, fg='red', bg='blue',text=self.Voicetext[tempi], width=40, height=2)
            self.Labelm[tempi] = tk.Label(self, fg='red', text=self.Voicetext[tempi], width=40, height=2,justify = LEFT)
            #self.Labelm.pack();
            self.Labelm[tempi].grid(row=tempi, rowspan=1,columnspan=2)
            self.Encrym[tempi] =  tk.Entry(self,width=60)
            self.Encrym[tempi].grid(row=tempi,  column=3,rowspan=1, columnspan=2, )

    def say_hi(self):
        print("hi there, everyone!")
        showme.showme()

    def UDTCustomer(self,clerk):
        while self.UDTCustomeLive:
            if self.ifRun:
                haha = clerk.get()
                print("UDT UI get 到了数据：（{}）".format(haha))
