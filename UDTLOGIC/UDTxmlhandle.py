import xml.sax
import threading,queue
from FILERead import Datachange

'''
<movie title="Enemy Behind">
   <UDTGETStart>MS Get UDTHeader</UDTGETStart>
   <UDTHeader>Get UDT Header</UDTHeader>
   <UDTBlock>UDT Block</UDTBlock>
   <UDTACK>Send a ACK PDU</UDTACK>
   <UDTTargetAddress>SAddr=</UDTTargetAddress>
   <UDTSourceAddress>DAddr=</UDTSourceAddress>
</movie>
'''

UDTstartString = 'fsafasdfasdfasdfasdf'
UDTHeaderString= ''
UDTBlockString= ''
UDTACKString= ''
UDTTargetAddress= ''
UDTSourceAddress= ''

ifUDTprintInput = 1

UDTstartStringSet = 'fsafasdfasdfasdfasdf'
UDTHeaderStringSet= ''
UDTBlockStringSet= ''
UDTACKStringSet= ''
UDTTargetAddressSet= ''

strOthersSet =''
strNOwaySet= ''
strEncryptornotSet =''
strSourceAddressSet = ''
strTargetAddressSet ='++'
strPersonalorGroup = ''
strUDT =''


class MovieHandler(xml.sax.ContentHandler):
    '''
    global UDTstartString
    global UDTHeaderString
    global UDTBlockString
    global UDTACKString
    global UDTTargetAddress
    global UDTSourceAddress
    '''
    def __init__(self):
        self.CurrentData = ""
        self.UDTGETStart = ""
        self.UDTHeader = ""
        self.UDTBlock = ""
        self.UDTACK = ""
        self.UDTTargetAddress = ""
        self.UDTSourceAddress = ""

    # 元素开始调用
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("***** UDT *****")
            title = attributes["title"]
            print("Title:", title)


    # 元素结束调用
    def endElement(self, tag):
        global UDTstartString
        global UDTHeaderString
        global UDTBlockString
        global UDTACKString
        global UDTTargetAddress
        global UDTSourceAddress
        if self.CurrentData == "UDTGETStart":
            print("UDTGETStart:", self.UDTGETStart)
            UDTstartString = self.UDTGETStart
            if ifUDTprintInput == 1:
                print("-->",UDTstartString)
        elif self.CurrentData == "UDTHeader":
            print("UDTHeader:", self.UDTHeader)
            UDTHeaderString = self.UDTHeader
            if ifUDTprintInput == 1:
                print(UDTHeaderString)

        elif self.CurrentData == "UDTBlock":
            print("UDTBlock:", self.UDTBlock)
            UDTBlockString = self.UDTBlock
            if ifUDTprintInput == 1:
                print(UDTBlockString)

        elif self.CurrentData == "UDTACK":
            print("UDTACK:", self.UDTACK)
            UDTACKString = self.UDTACK
            if ifUDTprintInput == 1:
                print(UDTACKString)

        elif self.CurrentData == "UDTTargetAddress":
            print("UDTTargetAddress:", self.UDTTargetAddress)
            UDTTargetAddress = self.UDTTargetAddress
            if ifUDTprintInput == 1:
                print(UDTTargetAddress)

        elif self.CurrentData == "UDTSourceAddress":
            print("UDTSourceAddress:", self.UDTSourceAddress)
            UDTSourceAddress = self.UDTSourceAddress
            if ifUDTprintInput == 1:
                print(UDTSourceAddress)
        self.CurrentData = ""

    # 读取字符时调用
    def characters(self, content):
        if self.CurrentData == "UDTGETStart":
            self.UDTGETStart = content
        elif self.CurrentData == "UDTHeader":
            self.UDTHeader = content
        elif self.CurrentData == "UDTBlock":
            self.UDTBlock = content
        elif self.CurrentData == "UDTACK":
            self.UDTACK = content
        elif self.CurrentData == "UDTTargetAddress":
            self.UDTTargetAddress = content
        elif self.CurrentData == "UDTSourceAddress":
            self.UDTSourceAddress = content

def CenenctStringToVar(sUDT,sPersonalorGroup,sSourceAddressSet,sTargetAddressSet,sEncryptornotSet,sOthersSet,sNOwaySet):
    global strOthersSet
    global strNOwaySet
    global strEncryptornotSet
    global strSourceAddressSet
    global strTargetAddressSet
    global strPersonalorGroup
    global strUDT
    strUDT              = sUDT
    strPersonalorGroup  = sPersonalorGroup
    strSourceAddressSet = sSourceAddressSet
    strTargetAddressSet = sTargetAddressSet
    strEncryptornotSet  = sEncryptornotSet
    strOthersSet        = sOthersSet
    strNOwaySet         = sNOwaySet


def UDTread():
    global strUDT
    return  strUDT

def UDTReadPersonalorGroup():
    global strPersonalorGroup
    return  strPersonalorGroup

def UDTReadstrSourceAddressSet():
    global strSourceAddressSet
    return  strSourceAddressSet

def UDTReadstrTargetAddressSet():
    global strTargetAddressSet
    return  strTargetAddressSet

def UDTReadEncryptornotSet():
    global strEncryptornotSet
    return  strEncryptornotSet

def UDTReadOthersSet():
    global strOthersSet
    return  strOthersSet
def UDTReadNOwaySet():
    global strNOwaySet
    return  strNOwaySet

def UDTFeedBack(inputString):
    global UDTstartString
    global UDTHeaderString
    global UDTBlockString
    global UDTACKString
    global UDTTargetAddress
    global UDTSourceAddress

    global strOthersSet
    global strNOwaySet
    global strEncryptornotSet
    global strSourceAddressSet
    global strTargetAddressSet
    global strPersonalorGroup
    global strUDT

    #print(UDTstartString)
    FindInMyVision = 1
    if UDTstartString in inputString:
        if ifUDTprintInput == 1:
            print("uuyiu",UDTstartString)
            print("UDTFeedback" + inputString)
    else:
        FindInMyVision = 0

    if UDTHeaderString in inputString:
        if ifUDTprintInput == 1:
            print("UDTFeedbackUDT header" + inputString)
        strUDT =inputString
    else:
        FindInMyVision = 0

    if UDTBlockString in inputString:
        if ifUDTprintInput == 1:
            print("UDTFeedback" + inputString)
        strOthersSet = inputString
    else:
        FindInMyVision = 0

    if UDTACKString in inputString:
        if ifUDTprintInput == 1:
            print("UDTFeedback" + inputString)
    else:
        FindInMyVision = 0

    if UDTTargetAddress in inputString:
        if ifUDTprintInput == 1:
            print("UDTADDress" + inputString)
        strTargetAddressSet = inputString
    else:
        FindInMyVision = 0


    if UDTSourceAddress in inputString:
        if ifUDTprintInput == 1:
            print("UDTSourceAddress" + inputString)
        strSourceAddressSet = inputString
    else:
        FindInMyVision = 0

    if FindInMyVision == 1:
        return inputString
    else:
        return ""


def UDTFeedBackThread(clearIN):
    global UDTstartString
    global UDTHeaderString
    global UDTBlockString
    global UDTACKString
    global UDTTargetAddress
    global UDTSourceAddress
    print(UDTstartString)
    inputString = clearIN.get()
    if UDTstartString in inputString:
        if ifUDTprintInput == 1:
            print("uuyiu",UDTstartString)
            print(inputString)
    elif UDTHeaderString in inputString:
        if ifUDTprintInput == 1:
            print(inputString)
    elif UDTBlockString in inputString:
        if ifUDTprintInput == 1:
            print(inputString)
    elif UDTACKString in inputString:
        if ifUDTprintInput == 1:
            print(inputString)

    elif UDTTargetAddress in inputString:
        if ifUDTprintInput == 1:
            print(inputString)

    elif UDTSourceAddress in inputString:
        if ifUDTprintInput == 1:
            print(inputString)


    return inputString
# 创建一个 XMLReader


def FirstRun():

    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    #parser.parse("movies.xml")
    #parser.parse("UDTSettingFile.xml")
    parser.parse('''C:\\Users\\chenzhuo\AILOGPDT\\UDTLOGIC\\UDTSettingFile.xml''')
    haha22 ="17E02300 Get UDT Header,UAB=0,PN=14 :40H, AH, 10H, 63H, 94H, 10H, 63H, 95H, 70H, 1AH, "
    UDTFeedBack(haha22)
    UDTFeedBack("17E0334E  Trunk System handle Event: Now State = 2 Now Event = 86. ")

    UDTFeedBack("PS Send a ACK PDU,SAddr=16517924,DAddr=16515092 ")



#FirstRun()