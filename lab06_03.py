#!/usr/bin/python

import os

path1 = 'output'
if os.path.exists(path1):
    print "list %s path" % path1
    print os.listdir(path1)

else :
    print "create %s path" % path1
    os.mkdir(path1)

print "Please input filename"
file1 = raw_input()
text = "This file was created with Python."

f1 = open(path1+"/"+file1,'w')
f1.write(text)
f1.close()

