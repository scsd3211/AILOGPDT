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
        self.strUDT = StringVar()
        self.strPersonalorGroup = StringVar()
        self.strSourceAddress = StringVar()
        self.strTargetAddress = StringVar()
        self.strEncryptornot = StringVar()
        self.strOthers = StringVar()
        self.strNOway= StringVar()
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
        '''
        for tempi in range(7):
            #self.Labelm[tempi] = tk.Label(self.root, fg='red', bg='blue',text=self.Voicetext[tempi], width=40, height=2)
            self.Labelm[tempi] = tk.Label(self, fg='red', text=self.Voicetext[tempi], width=40, height=2,justify = LEFT)
            #self.Labelm.pack();
            self.Labelm[tempi].grid(row=tempi, rowspan=1,columnspan=2)
            self.Encrym[tempi] =  tk.Entry(self,width=60)
            self.Encrym[tempi].grid(row=tempi,  column=3,rowspan=1, columnspan=2, )
        '''


        self.Labelm[0] = tk.Label(self, fg='red', text=self.Voicetext[0], width=40, height=2,justify = LEFT)
        self.Labelm[0].grid(row=0, rowspan=1,columnspan=2)
        self.Encrym[0] =  tk.Entry(self,width=60,textvariable=self.strUDT)
        self.Encrym[0].grid(row=0,  column=3,rowspan=1, columnspan=2, )

        self.Labelm[1] = tk.Label(self, fg='red', text=self.Voicetext[1], width=40, height=2,justify = LEFT)
        self.Labelm[1].grid(row=1, rowspan=1,columnspan=2)
        self.Encrym[1] =  tk.Entry(self,width=60,textvariable=self.strPersonalorGroup)
        self.Encrym[1].grid(row=1,  column=3,rowspan=1, columnspan=2, )

        self.Labelm[2] = tk.Label(self, fg='red', text=self.Voicetext[2], width=40, height=2,justify = LEFT)
        self.Labelm[2].grid(row=2, rowspan=1,columnspan=2)
        self.Encrym[2] =  tk.Entry(self,width=60,textvariable=self.strSourceAddress)
        self.Encrym[2].grid(row=2,  column=3,rowspan=1, columnspan=2, )

        self.Labelm[3] = tk.Label(self, fg='red', text=self.Voicetext[3], width=40, height=2,justify = LEFT)
        self.Labelm[3].grid(row=3, rowspan=1,columnspan=2)
        self.Encrym[3] =  tk.Entry(self,width=60,textvariable=self.strTargetAddress)
        self.Encrym[3].grid(row=3,  column=3,rowspan=1, columnspan=2, )

        self.Labelm[4] = tk.Label(self, fg='red', text=self.Voicetext[4], width=40, height=2,justify = LEFT)
        self.Labelm[4].grid(row=4, rowspan=1,columnspan=2)
        self.Encrym[4] =  tk.Entry(self,width=60,textvariable=self.strEncryptornot)
        self.Encrym[4].grid(row=4,  column=3,rowspan=1, columnspan=2, )

        self.Labelm[5] = tk.Label(self, fg='red', text=self.Voicetext[5], width=40, height=2,justify = LEFT)
        self.Labelm[5].grid(row=5, rowspan=1,columnspan=2)
        self.Encrym[5] =  tk.Entry(self,width=60,textvariable=self.strOthers)
        self.Encrym[5].grid(row=5,  column=3,rowspan=1, columnspan=2, )

        self.Labelm[6] = tk.Label(self, fg='red', text=self.Voicetext[6], width=40, height=2,justify = LEFT)
        self.Labelm[6].grid(row=6, rowspan=1,columnspan=2)
        self.Encrym[6] =  tk.Entry(self,width=60,textvariable=self.strNOway)
        self.Encrym[6].grid(row=6,  column=3,rowspan=1, columnspan=2, )

        #EncrymFile = tk.Entry(self,width=80,textvariable=self.Filee)
        #EncrymFile.grid(row=4, column=2, rowspan=1, columnspan=8, )

    def say_hi(self):
        print("hi there, everyone!")
        showme.showme()

    def UDTCustomer(self,clerk):
        while self.UDTCustomeLive:
            if self.ifRun:
                #print("UDT Customer Run")
                haha = clerk.get()
                print("UDT UI get 到了数据：（{}）".format(haha))
