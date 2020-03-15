#!/usr/bin/env python

import re


with open('ip-asn.txt') as f:
    log = f.read()
    reggie = r'\'latitude\':\s\d{1,3}.\d{1,4},'
    print(reggie)
    latline = re.findall(reggie, log)
    print(latline)
    
