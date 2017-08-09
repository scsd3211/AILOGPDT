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

class FileReadGetClass:
    ifRun = True
    FileReadCustomeLive = True
    def FileReadCustomer(self,clerk):
        while self.FileReadCustomeLive:
            if self.ifRun:
                haha = clerk.get()
                print("File获取到了数据：（{}）".format(haha))
    def SerialCustomerStop(self):
        self.ifRun = FALSE
        print("SerialCustomerStop")

    def SerialCustomerComtinue(self):
        self.ifRun = True
        print("SerialCustomerComtinue")

    def SerialCustomerliveDead(self):
        self.FileReadCustomeLive = False
        print("FileReadCustomeLiveDead")


class FileReadGetAndPutClass:
    ifRun = True
    FileReadCustomeLive = True
    UDTputClerk = 0
    PacketCleak = 0;
    VoiceCleak  = 0
    GPSCleark   = 0;


    def __init__(self, UDTC,PacketC, VoiceC, GPSC):
        self.UDTputClerk = UDTC
        self.PacketCleak = PacketC
        self.VoiceCleak= VoiceC
        self.GPSCleark = GPSC


    def FileReadCustomer(self,clerk):
        while self.FileReadCustomeLive:
            if self.ifRun:
                haha = clerk.get()
                if 1==2:
                    self.UDTputClerk.put(haha)
                    self.PacketCleak.put(haha)
                    self.VoiceCleak.put(haha)
                    self.GPSCleark.put(haha)

                print("File获取到了数据：（{}）".format(haha))
    def SerialCustomerStop(self):
        self.ifRun = FALSE
        print("SerialCustomerStop")

    def SerialCustomerComtinue(self):
        self.ifRun = True
        print("SerialCustomerComtinue")

    def SerialCustomerliveDead(self):
        self.FileReadCustomeLive = False
        print("FileReadCustomeLiveDead")

SerialCustomerME = SerialGetClass();

FileReadCustomer = FileReadGetClass();


print("run here")
clerk = queue.Queue(1);
clerkFile = queue.Queue(1)

UDTclerkFile = queue.Queue(1)
PacketclerkFile = queue.Queue(1)
VoiceclerkFile = queue.Queue(1)
GPSclerkFile = queue.Queue(1)

#将获取的数据分配给 每个模块
AllallocationFile = FileReadGetAndPutClass(UDTclerkFile,PacketclerkFile,VoiceclerkFile,GPSclerkFile)


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

appAIFileReadThreading = threading.Thread(target= appAILOG.FileReadAI,args=(clerkFile,))
#appAIFileReadGetThreading = threading.Thread(target= FileReadCustomer.FileReadCustomer,args=(clerkFile,))
appAIFileReadGetThreadingLast = threading.Thread(target= AllallocationFile.FileReadCustomer,args=(clerkFile,))


appAIFileReadThreading.start()
#appAIFileReadGetThreading.start()
appAIFileReadGetThreadingLast.start()


appVOICE = VOICEUIpy.Application(master=root)
#appUDT.pack(side=RIGHT)
appVOICE.place(bordermode=OUTSIDE, height=200, width=200,relheight = 0.5,relwidth =0.5,relx=0.3, rely=0.0)


appUDT = UDTUIpy.Application(master=root)
#appUDT.pack(side=RIGHT)
appUDT.place(bordermode=OUTSIDE, height=200, width=200,relheight = 0.5,relwidth =0.5,relx=0.6, rely=0.0)
appUDTFileReadThreading = threading.Thread(target= appUDT.UDTCustomer,args=(UDTclerkFile,))


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
