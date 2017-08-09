# -*- coding: cp936 -*-
from tkinter import *
from UI import packetLab
root = Tk()
root.title("hello world")
root.geometry('300x600')
ah = "adas"


Label(root, text='校训', font=('Arial', 20)).pack()

frm = Frame(root)
#left
frm_L = Frame(frm)
Label(frm_L,justify = 'right',text='厚德', font=('Arial', 15)).grid(row=0)
Label(frm_L, text='博23123学', font=('Arial', 15),justify = 'right').grid(row=1)
frm_L.pack(side=LEFT)

#right
frm_R = Frame(frm)
Label(frm_R, text='敬23423业', font=('Arial', 20),justify = 'right').grid(row=0)

Label(frm_R, text='狂2人', font=('Arial', 20),justify = 'right').grid(row=1)
Label(frm_R, text='乐群', font=('Arial', 20),justify = 'right').grid(row=2)
ww = packetLab.LabelMETEST(frm_R)
ww.LabelSet()
frm_R.pack(side=RIGHT)

#right
frm_RR = Frame(frm)
Label(frm_RR, text='敬32423业', font=('Arial', 20),justify =  "right").grid(row=4)

Label(frm_RR, text='狂人', font=('Arial', 20),justify = "right").grid(row=5)
Label(frm_RR, text='乐群22', font=('Arial', 20),justify = "right").grid(row=6)
ww = packetLab.LabelMETEST(frm_RR)
ww.LabelSet()
frm_RR.pack()




frm.pack()

root.mainloop()