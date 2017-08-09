import threading,queue
import time
import serial
from time import sleep
from Input import SerialInputClass


SerialClassME = SerialInputClass.SerialClass()
SerialClassME.start()
SerialClassME.SerialContinue()

class newer:
    a = 2
    b = 3

def producer(clerk):
    for product in range(10):
        new1 =newer()
        new1.a = product
        new1.b = product * 2
        clerk.put(new1)
        print("店员进货（{}）".format(product))

def customer(clerk):
    for product in range(20):
        haha = clerk.get()
        print("消费者买（{}）".format(haha.b))

def producer2(clerk):
    for product in range(10):
        new1 =newer()
        new1.a = product
        new1.b = product * 3
        clerk.put(new1)
        print("店员2进货（{}）".format(product))


def SerailCustomer(clerk):
    while True:
        haha = clerk.get()
        print("消费者买（{}）".format(haha))


print("run here")
clerk = queue.Queue(1);
SerialThreading = threading.Thread(target=SerialClassME.SerialGet,args=(clerk,))
SerailCustomthreading = threading.Thread(target=SerailCustomer,args=(clerk,))
#threading.Thread(target=producer,args=(clerk,)).start()
#threading.Thread(target=producer2,args=(clerk,)).start()
#threading.Thread(target=customer,args=(clerk,)).start()
SerialThreading.start()
SerailCustomthreading.start()

#SerailCustomthreading._stop()
print("over")


print("see you serial")