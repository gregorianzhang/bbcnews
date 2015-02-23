#!/usr/bin/python

import os

path1 = 'output'
if os.path.exists(path1):
    print "list %s path" % path1
    print os.listdir(path1)

else :
    print "create %s path" % path1
    os.mkdir(path1)
    print "list %s path" % path1
    print os.listdir(path1)
    print "rmdir %s path" % path1
    os.rmdir(path1)

# os.rmdir directory must empty



