import tkinter as tk
from tkinter import *
from UDTLOGIC import showme
import tkinter.filedialog
import threading,queue
from Input import SerialInputClass
from time import sleep



class Application(tk.Frame):


    def __init__(self, master=None , SerailProduce = None,SerailTarget=None):
        tk.Frame.__init__(self, master)
        self.Voicetext = ["AI日志分析系统 \nAI Log Analysis System", "Created by Zhuo Chen\n由陈卓创造", "\
专注于解决Hytera对讲机BUG\n\
Focus on solving Hytera the radio BUG", "","Encrypt or not", "Others",
                          "NO way"]
        self.Labelm = [1, 2, 3, 4, 5, 6, 7];
        self.Encrym = [1, 2, 3, 4, 5, 6, 7];
        self.root = master
        self.serialport = False
        self.logAnalyzeBool = False
        self.serialportCustomer = SerailProduce
        self.serialportClass     = SerailTarget
        self.Filee = StringVar()
        self.ComPort = StringVar()
        self.LogAnalyze = StringVar()
        self.pack()
        self.runFirst =1
        self.FileGetName= False;
        self.FileNameIs =''
        #self.createWidgets()
        self.packLabel()
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


        self.Labelm[0] = tk.Label(self, fg='red', text=self.Voicetext[0], width=40, height=2,)
        self.Labelm[0].grid(row=0,sticky= W,columnspan=4)

        self.Labelm[1] = tk.Label(self, fg='red', text=self.Voicetext[1], width=40, height=2)
        self.Labelm[1].grid(row=1,sticky= W ,columnspan=4)

        self.Labelm[2] = tk.Label(self, fg='red', text=self.Voicetext[2], width=40, height=2)
        self.Labelm[2].grid(row=2,sticky= W,columnspan=4)

        self.Labelm[3] = tk.Label(self, fg='red', text=self.Voicetext[3],width=40,  height=2, justify=LEFT)
        self.Labelm[3].grid(row=3, sticky=W,columnspan=4)


            #self.Encrym[tempi] =  tk.Entry(self)
            #self.Encrym[tempi].grid(row=tempi,  column=3,rowspan=1, columnspan=2, )
    def FileRead(self):
        print("FileRead")
        #print(u.get())
        fileReadTemp = tkinter.filedialog.askopenfilename(filetypes=[("*", "*")])
        try:
            self.Filee.set(fileReadTemp)
            print("File name is : " + fileReadTemp)
            self.FileNameIs = fileReadTemp
        except ValueError:
            print("no string")

        return fileReadTemp
    def FileReadAI(self,clerk):
        print("start File read AI")
        sleep(10)
        tempRunOrNot =1
        while tempRunOrNot:
            if self.FileNameIs != '':
                needfile = open(self.FileNameIs)
                lineneed = needfile.readline();
                while lineneed:
                    sleep(0.1)
                    if 1 == 1:
                        print(lineneed.strip())  # 后面跟 ',' 将忽略换行符
                    needhandlestr = lineneed.strip()
                    clerk.put(needhandlestr)

                    lineneed = needfile.readline()
                self.FileNameIs = ''

                print("File ---"+ self.FileNameIs + "has been dealt with")
                #tempRunOrNot =0

            else:
                sleep(3)


        sleep(10)
        tempcount =0;
        #print("****************(**&(*&(*&)()(*_(*)()(*&(*&(*&")
        while 0:
            halou = "count + " + str(tempcount)
            clerk.put(halou)
            tempcount = tempcount + 1
            sleep(0.2)
            print(halou)



    def SerialPortOpenClose(self):

        if self.serialport == False:
            print("Serial Open")
            try:
                #self.serialportThreading.start()
                #self.serialportGetTh.start()
                if self.runFirst == 1:
                    self.serialportClass.start()
                    self.runFirst = 2
                self.serialportCustomer.SerialCustomerComtinue()
                self.serialportClass.SerialContinue()
                self.ComPort.set("Start")
                self.serialport = True
            except ValueError:
                print("no string")
        else:
            print("Serial Close")
            try:
                #self.serialportThreading._stop()
                # self.serialportGetTh._stop()
                self.serialportCustomer.SerialCustomerStop()
                self.serialportClass.SerialStop()
                self.ComPort.set("Stop")
                self.serialport = False
            except ValueError:
                print("no string")

    def LogAnalyzeRun(self):
        print("LogAnalyze")
        if self.logAnalyzeBool:
            print("Serial dead  Open")
            self.LogAnalyze.set("Stop lala")
            self.logAnalyzeBool = False
            self.serialportClass.SerialDead()
            self.serialportCustomer.SerialCustomerliveDead()
        else:
            print("Serial dead  Run")
            self.logAnalyzeBool = True
            self.LogAnalyze.set("Run lala")


    def ComRead(self):
        print("FileRead")
        #print(u.get())

    def packBox(self):
        print("packBox")
        Button(self, text='File Open',command=self.FileRead).grid(row=4, sticky=W)
        EncrymFile = tk.Entry(self,width=80,textvariable=self.Filee)
        EncrymFile.grid(row=4, column=2, rowspan=1, columnspan=8, )

        Button(self, text='Serial COM',command= self.SerialPortOpenClose).grid(row=5, sticky=W)
        EncrymFile = tk.Entry(self,width=80,textvariable=self.ComPort)
        EncrymFile.grid(row=5, column=2, rowspan=1, columnspan=8, )

        Button(self, text=' Log Analyze ',command=self.LogAnalyzeRun).grid(row=6, sticky=W)
        EncrymFile = tk.Entry(self,width=80,textvariable=self.LogAnalyze)
        EncrymFile.grid(row=6, column=2, rowspan=1, columnspan=8, )
        #Button(self, text='Right').grid(row=6, sticky=W)
        #self.LogAnalyze.set("Stop lala")
        #filename = tkinter.filedialog.askopenfilename(filetypes=[("bmp格式", "bmp"), ("*", "*")])
        #print(filename)

    def say_hi(self):
        print("hi there, everyone!")
        showme.showme()
