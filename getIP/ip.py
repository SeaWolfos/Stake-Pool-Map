#!/usr/bin/env python

# BOOM BAM BABY IT WORKS

import re
from collections import Counter
reggie = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
f = open('../data/new.txt')
log = f.read()
iplist = re.findall(reggie,log)
with open("iplog.txt", "a") as iplog:
    for list in iplist:
        iplog.write(list +"\n")
        #print(list)

