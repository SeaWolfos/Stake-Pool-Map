#!/usr/bin/env python

f = open('new.txt')
lines = f.readlines()
for line in lines:
    print(line.split()[8])
