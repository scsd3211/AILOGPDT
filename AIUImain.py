#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as Tkinter
import time
import tkinter as tk
from UI import packetLab
#import Tkinter
'''
top = Tkinter.Tk()
# 进入消息循环
top.mainloop()
'''
LineSALl =8
MainWindows = tk.Tk(className='AI_UI_LOG_CHENZHUO')
#root = tk.Tk(className='AI_UI_LOG_CHENZHUO')

#MainWindows = tk.Frame(root)

class Window:
    def __init__(self, title='AI_UI_LOG_CHENZHUO', width=1024, height=600, staFunc=bool, stoFunc=bool):
        self.w = width
        self.h = height
        self.stat = True
        self.staFunc = staFunc
        self.stoFunc = stoFunc
        self.staIco = None
        self.stoIco = None
        self.Labelm =[1, 2, 3, 4, 5, 6, 7 ];
        self.Encrym = [1, 2, 3, 4, 5, 6, 7];
        self.Voicetext = ["Voice","Personal or Group","Source Address","Target Address","Encrypt or not","Others","NO way"]
        #self.root = tk.Tk(className=title)
        self.root = MainWindows
    def center(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int( (ws/2) - (self.w/2) )
        y = int( (hs/2) - (self.h/2) )
        self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))

    def packBtn(self):
        self.btnSer = tk.Button(self.root, command=self.event, width=15, height=2)
        #self.btnSer.pack(padx=20, side='left')
        self.btnSer.grid(row=LineSALl)
        btnQuit = tk.Button(self.root, text='关闭窗口', command=self.root.quit, width=15, height=2)
        #btnQuit.pack(padx=20, side='right')
        btnQuit.grid(row=LineSALl,column=1)
    def packLabel(self):
        #self.Label[0] = tk.Label()
        for tempi in range(7):
            #self.Labelm[tempi] = tk.Label(self.root, fg='red', bg='blue',text=self.Voicetext[tempi], width=40, height=2)
            self.Labelm[tempi] = tk.Label(self.root, fg='red', text=self.Voicetext[tempi], width=40, height=2)
            #self.Labelm.pack();
            self.Labelm[tempi].grid(row=tempi, rowspan=1,columnspan=2,)
            self.Encrym[tempi] =  tk.Entry(self.root)
            self.Encrym[tempi].grid(row=tempi,  column=3,rowspan=1, columnspan=2, )

        packetLab.LabelME(self.root)
        LabelReal = packetLab.LabelMEClass(self.root)
        LabelReal.LabelSet();



    def event(self):
        self.btnSer['state'] = 'disabled'
        if self.stat:
            if self.stoFunc():
                self.btnSer['text'] = '启动服务'
                self.stat = False
                self.root.iconbitmap(self.stoIco)
        else:
            if self.staFunc():
                self.btnSer['text'] = '停止服务'
                self.stat = True
                self.root.iconbitmap(self.staIco)
        self.btnSer['state'] = 'active'

    def loop(self):
        self.root.resizable(False, False)   #禁止修改窗口大小
        self.packBtn()
        self.center()                       #窗口居中
        self.packLabel()
        self.event()
        self.root.mainloop()

########################################################################
def sta():
    print('start.')
    return True
def sto():
    print('stop.')
    return True

if __name__ == '__main__':
    import sys, os

    w = Window(staFunc=sta, stoFunc=sto)
    w.staIco = os.path.join(sys.exec_prefix, 'DLLs\pyc.ico')
    w.stoIco = os.path.join(sys.exec_prefix, 'DLLs\py.ico')

    w.loop()
    #root.mainloop()