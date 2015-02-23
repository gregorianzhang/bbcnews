#!/usr/bin/python

import urllib2

print "Please input url"
url = raw_input()

www=urllib2.urlopen(url)
context = www.read()
print context
