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
import threading,queue
import time
import serial
from time import sleep
from Input import SerialInputClass

class newer:
    a = 2
    b = 3

SerialClassME = SerialInputClass.SerialClass()
class SerialGetClass:
    ifRun = False
    SerialCustomeLive = True
    def SerailCustomer(self,clerk):
        while self.SerialCustomeLive:
            if self.ifRun:
                haha = clerk.get()
                print("获取到了数据：（{}）".format(haha))
    def SerialCustomerStop(self):
        self.ifRun = FALSE
        print("SerialCustomerStop")

    def SerialCustomerComtinue(self):
        self.ifRun = True
        print("SerialCustomerComtinue")

    def SerialCustomerliveDead(self):
        self.SerialCustomeLive = False
        print("SerialCustomerliveDead")

SerialCustomerME = SerialGetClass();

print("run here")
clerk = queue.Queue(1);
SerialThreading = threading.Thread(target=SerialClassME.SerialGet,args=(clerk,))
SerailCustomthreading = threading.Thread(target=SerialCustomerME.SerailCustomer,args=(clerk,))
#threading.Thread(target=producer,args=(clerk,)).start()
#threading.Thread(target=producer2,args=(clerk,)).start()
#threading.Thread(target=customer,args=(clerk,)).start()
SerialThreading.start()
SerailCustomthreading.start()

root = tk.Tk(className='\AI_UI_LOG_CHENZHUO')
root.geometry('1600x800')
appAILOG = AILOGUIpy.Application(master=root,SerailProduce=SerialCustomerME,SerailTarget=SerialClassME )
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
print("run here")

#threading.Thread(target=producer,args=(clerk,)).start()
#threading.Thread(target=producer2,args=(clerk,)).start()
#threading.Thread(target=customer,args=(clerk,)).start()


root.mainloop()
