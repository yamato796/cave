import sys
import re

in_file = open(sys.argv[1], "r", encoding='UTF-16')
#in_file = open(sys.argv[1], "r")
out_file = open(sys.argv[1]+"out.txt", "w", encoding='UTF-16')

for line in in_file:
    lines = re.split(r'\.|\?', line)
    for l in lines:
        if(l.strip()!=""):
            out_file.write((l.strip()+"\n"))

in_file.close()
out_file.close()
