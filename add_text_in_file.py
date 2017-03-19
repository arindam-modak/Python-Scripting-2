import time as t
from os import path

def createFile(para):

    date=t.localtime(t.time())
    ##file name=month_day_year
    name='%d_%d_%d.txt'%(date[1],date[2],(date[0]))

    if not (path.isfile(para + name)):
        f=open(para + name,'w')
        f.write('\n'*2)
        a=raw_input("enter text: ")
        f.write(a)
        f.close()

if __name__=='__main__':
    destination='C:\\Users\\arindam das modak\\Desktop\\python scripting\\'
    ## this is to add a backslash '\' we use '\\' as single '\' is used for escape sequence

    createFile(destination)
    raw_input("Create file")
