# -*- coding: cp936 -*-
from tkinter import *
from UI import packetLab
root = Tk()
root.title("hello world")
root.geometry('300x600')
ah = "adas"


Label(root, text='Уѵ', font=('Arial', 20)).pack()

frm = Frame(root)
#left
frm_L = Frame(frm)
Label(frm_L,justify = 'right',text='���', font=('Arial', 15)).grid(row=0)
Label(frm_L, text='��23123ѧ', font=('Arial', 15),justify = 'right').grid(row=1)
frm_L.pack(side=LEFT)

#right
frm_R = Frame(frm)
Label(frm_R, text='��23423ҵ', font=('Arial', 20),justify = 'right').grid(row=0)

Label(frm_R, text='��2��', font=('Arial', 20),justify = 'right').grid(row=1)
Label(frm_R, text='��Ⱥ', font=('Arial', 20),justify = 'right').grid(row=2)
ww = packetLab.LabelMETEST(frm_R)
ww.LabelSet()
frm_R.pack(side=RIGHT)

#right
frm_RR = Frame(frm)
Label(frm_RR, text='��32423ҵ', font=('Arial', 20),justify =  "right").grid(row=4)

Label(frm_RR, text='����', font=('Arial', 20),justify = "right").grid(row=5)
Label(frm_RR, text='��Ⱥ22', font=('Arial', 20),justify = "right").grid(row=6)
ww = packetLab.LabelMETEST(frm_RR)
ww.LabelSet()
frm_RR.pack()




frm.pack()

root.mainloop()