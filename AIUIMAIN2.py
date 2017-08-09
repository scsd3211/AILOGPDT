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
#MainWindows = tk.Tk(className='AI_UI_LOG_CHENZHUO')


class Window:
    def __init__(self, MainFrame , width=1024, height=600, staFunc=bool, stoFunc=bool):
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
        self.root = MainFrame
    def packLabel(self):
        #self.Label[0] = tk.Label()
        for tempi in range(7):
            #self.Labelm[tempi] = tk.Label(self.root, fg='red', bg='blue',text=self.Voicetext[tempi], width=40, height=2)
            self.Labelm[tempi] = tk.Label(self.root, fg='red', text=self.Voicetext[tempi], width=40, height=2)
            #self.Labelm.pack();
            self.Labelm[tempi].grid(row=tempi, rowspan=1,columnspan=2,)
            self.Encrym[tempi] =  tk.Entry(self.root)
            self.Encrym[tempi].grid(row=tempi,  column=3,rowspan=1, columnspan=2, )
            #LabelME()

    def loop(self):

        self.packLabel()


########################################################################
def sta():
    print('start.')
    return True
def sto():
    print('stop.')
    return True

if __name__ == '__main__':
    import sys, os

    root = tk.Tk(className='AI_UI_LOG_CHENZHUO')
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = int((ws / 2) - (1024 / 2))
    y = int((hs / 2) - (600 / 2))
    root.geometry('{}x{}+{}+{}'.format(1024, 600 ,x, y))
    MainWindows = tk.Frame(root)
    w = Window(MainFrame =MainWindows ,staFunc=sta, stoFunc=sto)


    w.loop()
    root.mainloop()