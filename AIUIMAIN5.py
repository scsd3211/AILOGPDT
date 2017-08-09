import tkinter as tk
from tkinter import *
import tkinter.filedialog
from UI import packetFrame
from UI import GPSUIpy
from UI import PACKETUIpy
from UI import AILOGUIpy
from UI import UDTUIpy
from UI import VOICEUIpy
from UI import OTHERSUIpy


root = tk.Tk(className='\AI_UI_LOG_CHENZHUO')
root.geometry('1600x800')
appAILOG = AILOGUIpy.Application(master=root)
appAILOG.place(bordermode=OUTSIDE, height=100, width=100,relheight = 0.5,relwidth =0.5,relx=0.0, rely=0.0)
appAILOG.packBox()

appVOICE = VOICEUIpy.Application(master=root)
#appUDT.pack(side=RIGHT)
appVOICE.place(bordermode=OUTSIDE, height=200, width=200,relheight = 0.5,relwidth =0.5,relx=0.3, rely=0.0)


appUDT = UDTUIpy.Application(master=root)
#appUDT.pack(side=RIGHT)
appUDT.place(bordermode=OUTSIDE, height=200, width=200,relheight = 0.5,relwidth =0.5,relx=0.6, rely=0.0)

appPACKET = PACKETUIpy.Application(master=root)
appPACKET.place(bordermode=OUTSIDE, height=100, width=100,relheight = 0.5,relwidth =0.5,relx=0.0, rely=0.5)

appGPS = GPSUIpy.Application(master=root)
#appUDT.pack(side=RIGHT)
appGPS.place(bordermode=OUTSIDE, height=200, width=200,relheight = 0.5,relwidth =0.5,relx=0.3, rely=0.5)


appOTHERS = OTHERSUIpy.Application(master=root)
#appUDT.pack(side=RIGHT)
appOTHERS.place(bordermode=OUTSIDE, height=200, width=200,relheight = 0.5,relwidth =0.5,relx=0.6, rely=0.5)

#app.mainloop()
root.mainloop()
