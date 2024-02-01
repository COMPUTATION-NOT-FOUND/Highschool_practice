import struct
import os

class sRectype:
    def __init(self):
        self.stID=0
        self.stuname=''
        self.stuclass=''
        self.stufee=0.0
myrec=sRectype()
recformat="i20s4sf"
recsize=struct.calcsize(recformat)
print(recsize)

file=open("randomfiling.Dat",'a+b')
file.seek(0,os.SEEK_END)
totalrecs=file.tell()/recsize

myrec.stid=
