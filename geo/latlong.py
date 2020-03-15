#!/usr/bin/env python

import re
import json

with open('ip-asn.txt') as f:
    log = f.read()
#    reggie = r'\'\w{8,9}\':\s\d{1,3}.\d{1,4},' # latitude and longitude regex
#    latline = re.findall(reggie, log) # find &  put them in a variable
    ipreg = r'\'ip\':\s\'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' # pool ip regex
    ipLine = re.findall(ipreg, log) # find ip by regex
    
    # parse out latitude
    latreg = r'\'latitude\':\s\d{1,3}.\d{1,4},' #pulls latitude line
    latLine = re.findall(latreg, log)
    print(latLine)
    numsOnlyReg = r'\d{1,3}.\d{1,4}'
    lat = re.findall(numsOnlyReg, latLine)
    print(lat)

    longireg = r'\'longitude\':\s\d{1,3}.\d{1,4},' #pulls longitude line
    longiLine = re.findall(longireg, log)
    longi = re.findall(numsOnlyReg, longiLine)
    print(longi)

    pools = {} # dict
    pools['pool'] = []
    pools['pool'].append({
        'name': '',
        'ticker': '',
        'website': '',
        'ip': ip,
        'latitude': lat,
        'longitude': longi,
        })

    print(pools)

       # latlong.write('\n'.join(latline))
       
