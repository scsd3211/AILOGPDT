# -*- coding: cp936 -*-
from tkinter import *
root = Tk()
root.title("hello world")
root.geometry('300x200')
ah = "adas"


Label(root, text='Уѵ', font=('Arial', 20)).pack()

frm = Frame(root)
#left
frm_L = Frame(frm)
Label(frm_L, text='���', font=('Arial', 15)).pack(side=TOP)
Label(frm_L, text='��ѧ', font=('Arial', 15)).pack(side=TOP)
frm_L.pack(side=LEFT)

#right
frm_R = Frame(frm)
Label(frm_R, text='��ҵ', font=('Arial', 15)).pack(side=TOP)
Label(frm_R, text='��Ⱥ', font=('Arial', 15)).pack(side=TOP)
frm_R.pack(side=RIGHT)

frm.pack()

root.mainloop()