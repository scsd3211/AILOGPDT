from FILERead import Datachange
haah ="17E03353 Get UDT Block1: 35H, 32H, 33H, FFH, FFH, FFH, FFH, FFH, FFH, FFH, 1EH, 76H, "
Strin = Datachange.ALLData(haah,haah)


class UDTHandleClass:
    ToAPPLaterHandle = 0;
    ifprintshow = 1
    def UDTdataHandle(self,String):
        if 'UDTHeader' in String.SpecialStr:
            if self.ifprintshow== 1:
                print("UDTHeader", String.DataContent)

            return String.DataContent

        elif 'UDT Header' in String.SpecialStr:
            if self.ifprintshow == 1:
                print("UDT Header", String.DataContent)
            return String.DataContent

        elif 'UDT Block' in String.SpecialStr:
            if self.ifprintshow == 1:
                print("UDT Block", String.DataContent)
            return String.DataContent

        elif 'Give APP UDT Format' in String.SpecialStr:
            if self.ifprintshow == 1:
                print("Give APP UDT Format", String.DataContent)
            self.ToAPPLaterHandle = 1
            return String.DataContent
        elif 'PS Send a ACK PDU' in String.SpecialStr and self.ToAPPLaterHandle == 1:
            if self.ifprintshow == 1:
                print("PS Send a ACK PDU", String.DataContent)
            return String.DataContent

        else:
            print("not compare")

    def UDTdataNoprint(self,ifPrintInt =0):
        self.ifprintshow = ifPrintInt


def showme():
    print("show me")







tutu ="17E02300 Get UDT Header,UAB=0,PN=14 :40H, AH, 10H, 63H, 94H, 10H, 63H, 95H, 70H, 1AH, "
tutuS = Datachange.ALLData(tutu,tutu)
tutu1 ="17E03389 Short Data,Give APP UDT Format:10 Data:3235H,"
tutu1S = Datachange.ALLData(tutu1,tutu1)
tutu2 ="17E03392  PS Send a ACK PDU,SAddr=1074068,DAddr=1074069"
tutu2 = Datachange.ALLData(tutu2,tutu2)

UDTC = UDTHandleClass()

UDTC.UDTdataHandle(tutuS)
#UDTC.UDTdataHandle(tutu1S)
UDTC.UDTdataHandle(tutu2)



