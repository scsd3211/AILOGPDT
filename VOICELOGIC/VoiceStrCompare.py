
CountVoiceFrame =[0]*217
def compareHowMany(a,b):
    tempCount =0;
    c = a^b
    if(c  !=  0):
        for i in range(0,4):
            j = c>>i & 0x1
            if(j == 1):
                tempCount = tempCount +1;
    else:
        pass

    return tempCount

def compareVoiceFrame(aStr,bStr,intleng):
    intTotalDiff = 0
    for i in range(0,intleng):
        if(i >= 27 and i <= 38):
            continue
        try:
            aint1 = int(aStr[i], 16)
            bint1 = int(bStr[i], 16)
            ComR = compareHowMany(aint1, bint1)
            intTotalDiff = intTotalDiff + ComR
        except ValueError:
            print("something is not ABC")
    return intTotalDiff;

def StrNOempty(strIN):
    strIN = strIN.replace(" ",'')
    return strIN;

def StrVoiceFrameget(VoiceFrame):
    intRssi = VoiceFrame.find("RSSI=")
    intState = VoiceFrame.find("State=")
    if(intRssi != -1):
        #print("intRssi =%d" %intRssi)
        strTemp1 = VoiceFrame[intRssi + 10:intRssi + 10 + 89]
        #pass
    elif(intState != -1):
        #print("intState =%d" %intState)
        strTemp1 = VoiceFrame[intState + 10:intState + 10 + 89]
    else:
        return  -1

    return strTemp1;

def VoiceFrameError(intPNUM):
    intCC = intPNUM/4
    print(intCC)
    intCC = int(intCC)
    print(intCC)
    CountVoiceFrame[intCC] = CountVoiceFrame[intCC] + 1

    return 0;

def VoiceFrameRead():

    return CountVoiceFrame;