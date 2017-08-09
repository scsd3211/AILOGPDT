import tkinter as tk
from tkinter import *
from UI import packetFrame


root = tk.Tk()
root.geometry('1600x600')
app = packetFrame.Application(master=root)
app.place(bordermode=OUTSIDE, height=100, width=100,relheight = 0.5,relwidth =0.5,relx=0.0, rely=0.5)

appUDT = packetFrame.Application(master=root)
#appUDT.pack(side=RIGHT)
appUDT.place(bordermode=OUTSIDE, height=200, width=200,relheight = 0.5,relwidth =0.5,relx=0.3, rely=0.5)


appPACKET = packetFrame.Application(master=root)
#appUDT.pack(side=RIGHT)
appPACKET.place(bordermode=OUTSIDE, height=200, width=200,relheight = 0.5,relwidth =0.5,relx=0.6, rely=0.5)

#app.mainloop()
root.mainloop()
