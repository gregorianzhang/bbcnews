#!/usr/bin/python 

import os

list1 = {"txt" : "Text file", "rtf" : "Rich Text File", "doc" : "MS Word document", "pdf"  : "Adobe Portable Document File", "htm" : "HTML file", "html": "HTML file", "jpg" : "JPEG Image file", "jpeg" : "JPEG Image file", "bmp" : "Bitmap Image file", "exe" : "Windows executable file", "dll" : "Windows library file"}

system1 = ""

if os.name == 'nt':
    system1 = "windows"
elif os.name == 'mac':
    system1 = "mac"
elif os.name == "posix":
    system1 = "linux"
else:
    system1 = "unknow"

def file_extension(path):
    list = os.listdir(path)
    for a in list:
        # file is true
        num = a.rfind(".")
        try:
            typefile = list1[a[-3:]]
        except:
            typefile = "Unknow Filetype"

        print "Filename: %50s Extension: %10s Filetype: %20s " % (a[0:num],a[-3:],typefile)

print "Please input file name"
file1 = raw_input()
print "Please input your user name"
user1 = raw_input()

if system1 == "windows":
#    list = os.listdir('c:/Windows')
#    with open(file1,'w') as f:
#        for a in list:
#            f.write(a+"\n")
    file_extension('c:/Windows')

elif system1 == "linux":
#    list = os.listdir('/Users/'+user1+ '/Documents')
#    list = os.listdir('/home/'+user1+ '/Downloads')
#    with open(file1,'w') as f:
#        for a in list:
#            f.write(a+"\n")
    file_extension('/home/'+user1+ '/Downloads')

elif system1 == "mac":
    file_extension('/Users/'+user1+ '/Documents')


