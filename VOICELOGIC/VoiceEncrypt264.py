import os

import sys
from VOICELOGIC import VoiceStrCompare

print("Voice logic run")
print(VoiceStrCompare.compareHowMany(2,5))

class StringSearchClass:
    pSwitch = 1;
    flagSwtich = 1;
    iffileprint =0;
    #f = open(".\packet\\voiceconfig.txt")
    f = None
    f264configFile = None
    DirecSourceFile = ".\shenzhen0423\\"

    DirecResultFile = ".\\result\\"
    RxVoice = "Rx Voice:"

    StandardSilenceFrame = "8C40E90D8DB43020008C40E90D8755FD7DF75F7DB43020008C40E90D8DB4302000008C40"
    SmallFile = open(DirecResultFile + "smallVoice2.txt", 'w')
    # needfile = open("0304/rrrrr.txt")
    # SmallFile.close()

    needhandlestr = "1996500  Trunk Rx Voice:F,State=11  84C4 B05D 0A33 E8F9 95F0 AB30 C203 0000 0000 0554 2854 3F05 5917 95B5 14BE EABC F300 84C4"
    line = ''

    line264 =''



    def fileReady(self):
        CurrentDir = os.getcwd()
        print(CurrentDir)
    
    
        self.f = open(".\config\configVoiceSlienceFrame.txt","r")             # 返回一个文件对象

        self.f.seek(0, 0)
        self.line = self.f.readline()

        self.f264configFile = open(".\config\configVoice264Frame.txt","r")             # 返回一个文件对象
        self.f264configFile.seek(0,0)
        self.line264 = self.f264configFile.readline();

        
        if(os.path.exists(self.DirecResultFile) == True):
            print("Dirce is exist%s"%self.DirecResultFile)
        else:
            os.mkdir(self.DirecResultFile)
            print("create directory %s"%self.DirecResultFile)
    

    def SearchOneString(self,line2):
        # print(line.strip())  # 后面跟 ',' 将忽略换行符
        self.needhandlestr = line2
        configstring = self.line.strip()
        if not configstring:
            return
        if self.pSwitch == 1:
            print("TEst")
            print(configstring)
        if configstring in self.needhandlestr:
            if self.flagSwtich == 1:
                print("^^^^^^^")
            if self.iffileprint == 0:
                print("%s------ %d"%(self.needhandlestr,len(self.needhandlestr)))
                if self.RxVoice in self.needhandlestr:
                    intlengNeed =len(self.needhandlestr)

                    if(intlengNeed > 120 and intlengNeed < 130):
                        tempStrget= VoiceStrCompare.StrVoiceFrameget(self.needhandlestr)
                        if(tempStrget == -1):
                            pass
                        else:
                            tempStrget =VoiceStrCompare.StrNOempty(tempStrget)
                            tempStrlen = len(tempStrget)
                            standardlen = len(self.StandardSilenceFrame)
                            if(tempStrlen != standardlen):
                                print("length is not same")
                                pass
                            else:
                                howManyDifInt = VoiceStrCompare.compareVoiceFrame(tempStrget,self.StandardSilenceFrame,len(self.StandardSilenceFrame)-6);
                                if(howManyDifInt == -1):
                                    pass
                                else:
                                    print("%s------ %d--+++%s--diff==%d" % (self.needhandlestr, len(self.needhandlestr),tempStrget,howManyDifInt))
                                    VoiceStrCompare.VoiceFrameError(howManyDifInt);
                                    if(howManyDifInt <= 80):
                                        self.SmallFile.write(self.needhandlestr+"----diff=="+ str(howManyDifInt)+"\n")


            else:
                self.ff.write(self.needhandlestr + "\n")

            if self.flagSwtich == 1:
                print("%%%%%%%%%")
        # print(line, end = '')　　　# 在 Python 3中使用

        #line = self.f.readline()





    

    
#SearchOneString(line)
    
#SmallFile.close()
    #print(VoiceStrCompare.VoiceFrameRead());



    def Search264String(self, line2):
        # print(line.strip())  # 后面跟 ',' 将忽略换行符
        self.needhandlestr = line2
        while self.line264:
            configstring = self.line264.strip()
            if self.pSwitch == 9:
                print("TEst264")
                print(configstring)
            if configstring in self.needhandlestr:
                print(self.needhandlestr)

            self.line264 = self.f264configFile.readline()

        self.f264configFile.seek(0, 0)
        self.line264 = self.f264configFile.readline()

                # line = self.f.readline()

    # SearchOneString(line)

    # SmallFile.close()

    def SearchStringReadNext(self,line3):
        while self.line:
            self.SearchOneString(line3)
            self.line = self.f.readline()

okstet = StringSearchClass()
okstet.fileReady()
#okstet.SearchOneString("1996500  Trunk Rx Voice:F,State=11  84C4 B05D 0A33 E8F9 95F0 AB30 C203 0000 0000 0554 2854 3F05 5917 95B5 14BE EABC F300 84C4")
#okstet.SearchOneString("16D8BF1  Trunk Rx Voice:A,RSSI=-80  8C41 E90D 8DB4 3020 008C 40E9 0D87 55FD 7DF7 5F7D B430 2000 8C40 E90D 8DB4 3020 0000 8C61")

okstet.SearchStringReadNext("16D8BF1  Trunk Rx Voice:A,RSSI=-80  8C49 E90D 8DB4 3020 008C 40E9 0D87 55FD 7DF7 5F7D B430 2000 8C40 E90D 8DB4 3020 0000 8C61")

okstet.Search264String("16D8BF1  Trunk Rx Voice:A,RSSI=-80  8C49 E90D 8DB4 3020 008C 40E9 0D87 55FD 7DF7 5F7D B430 2000 8C40 E90D 8DB4 3020 0000 8C61")

okstet.Search264String("C5905C Trunk Rx Voice:B,State=11  C673 5512 6FAF 77DE 13E6 A0CE 48B3 B06B BA37 1AF5 5F3B C629 8253 BDE6 AECD CD65 E400 C673")
'''
print("over")
    #needfile = open("testcour.txt")
'''



