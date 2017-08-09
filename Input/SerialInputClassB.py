import time
import serial
from time import sleep
import threading,queue
class SerialClass:
    ser  =serial.Serial( #下面这些参数根据情况修改
        port='COM4',
        baudrate=115200,         #9600,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.SEVENBITS
    )
    data = ''
    RunGO = False
    ThreadLive = True
    LastKeepStr =''
    def start(self):
        self.ser =serial.Serial( #下面这些参数根据情况修改
        port='COM4',
        baudrate=115200,         #9600,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.SEVENBITS
    )
    def recv(self,serial):
       data1 = ''
       while True:
           data1 =serial.read(300)
           if data1 == '':
               continue
           else:
               break
           sleep(0.02)
       return data1
    def StringUinon(self,stringIn,clerk):
        info = stringIn

        #print("****************(**&(*&(*&)()(*_(*)()(*&(*&(*&")
        while 1:
            kk = info.find('\n')
            if kk != -1:
                kStr = self.LastKeepStr + info[0:kk]
                kkS = kk + 1;
                info = info[kkS:]

                #print(kStr)
                clerk.put(kStr)
                print("店员进货（{}）".format(kStr))

            else:
                self.LastKeepStr = info[0:]
                break
    def SerialGet(self,clerk):
        while self.ThreadLive:
            if self.RunGO:
               data2 = ''
               data2 =self.recv(self.ser)
               #ser.write(data2)
               #print(data2)
               c = data2.decode(encoding='utf-8')
               self.StringUinon(c,clerk)
               #print(c,end='')


    def SerialStop(self):
         self.RunGO = False
         print("Seriial Stop")

    def SerialContinue(self):
         self.RunGO = True
         print("Seriial Coptinue")

    def SerialDead(self):
        self.ThreadLive = False
        print("Seriial ThreadLive dead")

#SerialGet()
#Serialthreadhandle = threading.Thread(target=SerialGet)
#Serialthreadhandle.start()