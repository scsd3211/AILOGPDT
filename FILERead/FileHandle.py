import os

class FileAllHanlde:
    whichFileHandle =''
    needfile = ''
    def __init__(self,filenameIn = 0):
        self.needfile = open(filenameIn)

    def config(self,filenamein):
        self.whichFileHandle = filenamein
        #needfile = open(".\shenzhen0423\\" + filenamein)
        self.needfile = open(self.whichFileHandle)

    def ReadMyFileLine(self):
        lineneed = self.needfile.readline();
        return lineneed

    def CloseMyFile(self):
        self.needfile.close()

    def FielReadSeekZero(self):
        self.needfile.seek(0,0)
