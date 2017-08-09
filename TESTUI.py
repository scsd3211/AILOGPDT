import tkinter as Tkinter
import time
import tkinter as tk


widthLeng = 1024
heighlength = 600
master = tk.Tk()
w = tk.Canvas(master, width=widthLeng, height=heighlength)
w.pack()


'''
w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
'''
w.create_rectangle(0, 0, widthLeng, heighlength, fill="blue")

master.mainloop()