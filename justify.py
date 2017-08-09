# 这样我就不用写 tkinter
from tkinter import *

root = Tk()  # 注意Tk的大小写

#photo = PhotoImage(file=‘1.png‘)
theLabel = Label(root,text='博客园\n舍名利 - --',justify = LEFT)

theLabel.pack()

theLabel = Label(root,text='2323博客园\n舍名利 - --',justify = LEFT)

theLabel.pack()

theLabel = Label(root,text='博客23423园\n舍名利 - --',justify = LEFT)

theLabel.pack()

theLabel = Label(root,text='博客34534园\n舍345名利 - --',justify = LEFT)

theLabel.pack()
root.mainloop()


