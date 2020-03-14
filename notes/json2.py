#!/usr/bin/python

f = open('/home/cam/logs/node.out')

for line in iter(f):
    ip = line.split(":")[3]
    if ip == strUsrinput:
        print(line)

f.close()

