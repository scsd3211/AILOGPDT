import tkinter as tk
import tkinter
import sys, os


top = tkinter.Tk()


class Window:
    def __init__(self, title='AI_UI_LOG_CHENZHUO', width=1900, height=1000, staFunc=bool, stoFunc=bool):
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
        self.root = top

    def center(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int((ws / 2) - (self.w / 2))
        y = int((hs / 2) - (self.h / 2))
        self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))



    def packLabel(self):
        # self.Label[0] = tk.Label()
        for tempi in range(7):
            # self.Labelm[tempi] = tk.Label(self.root, fg='red', bg='blue',text=self.Voicetext[tempi], width=40, height=2)
            self.Labelm[tempi] = tk.Label(self.root, fg='red', text=self.Voicetext[tempi], width=40, height=2)
            # self.Labelm.pack();
            self.Labelm[tempi].grid(row=tempi, rowspan=1, columnspan=2, )
            self.Encrym[tempi] = tk.Entry(self.root)
            self.Encrym[tempi].grid(row=tempi, column=3, rowspan=1, columnspan=2, )




    def loop(self):
        self.root.resizable(False, False)  # 禁止修改窗口大小

        self.center()  # 窗口居中
        #self.packLabel()

        #self.root.mainloop()

def sta():
    print('start.')
    return True
def sto():
    print('stop.')
    return True

B = tkinter.Button(top, text ="Hello")

B.pack()
B.place( height=200, width=200)
w = Window(staFunc=sta, stoFunc=sto)
w.loop()
top.mainloop()