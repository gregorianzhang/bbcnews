#!/usr/bin/python

outfile = "lab01.txt"
text = "This file was created with Python."

file1 = open(outfile,'w')
file1.write(text)
file1.close()


outfile1 = "lab01_1.txt"
with open(outfile1,'w') as file2:
    file2.write(text)

# no need files.close()

