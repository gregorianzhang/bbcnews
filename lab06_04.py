#!/usr/bin/python 

import os


system1 = ""

if os.name == 'nt':
    system1 = "windows"
elif os.name == 'mac':
    system1 = "mac"
elif os.name == "posix":
    system1 = "linux"
else:
    system1 = "unknow"



print "Please input file name"
file1 = raw_input()
print "Please input your user name"
user1 = raw_input()

if system1 == "windows":
    list = os.listdir('c:/Windows')
    with open(file1,'w') as f:
        for a in list:
            f.write(a+"\n")

elif system1 == "linux":
    list = os.listdir('/Users/'+user1+ '/Documents')
#    list = os.listdir('/home/'+user1+ '/Downloads')
    with open(file1,'w') as f:
        for a in list:
            f.write(a+"\n")

