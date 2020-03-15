#!/usr/bin/env python

import re
import json

# open up geo data from API
with open('ip-asn.txt') as f:
    # read file
    log = f.read()

    # regex for ip line
    ipreg = r'\'ip\':\s\'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    # pull ip line from log
    ipLine = re.findall(ipreg, log) 
    print('ipLine is: ', ipLine)
    print('type of ipLine is ', type(ipLine))
    # convert ipLine to string
    ipLineStr = ' '.join([str(elem) for elem in ipLine])
    print('ipLineStr: ', ipLineStr)
    print('ipLineStr type: ', type(ipLineStr))

    # regex to pull IP addr only
    ipOnlyReg = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    # pull IP only
    ipList = re.findall(ipOnlyReg, ipLineStr)
    ip = ' '.join([str(elem) for elem in ipList])
    print('ip: ', ip)
    print('ip type: ', type(ip))

    # regex to parse out latitude from log
    latreg = r'\'latitude\':\s\d{1,3}.\d{1,4},' 
    # pull latitude from log
    latLine = re.findall(latreg, log)
    print('latLine: ', latLine)
    print('latLine type: ', type(latLine))
    # convert latLine to string
    latLineStr = ' '.join([str(elem) for elem in latLine])
    print('latLineStr; ', latLineStr)
    print('latLineStr type: ', type(latLineStr))

    # regex pull out lat/long numbers from entire lines
    numsOnlyReg = r'\d{1,3}.\d{1,4}'
    # pull lat number
    latList = re.findall(numsOnlyReg, latLineStr)    
    lat = ' '.join([str(elem) for elem in latList])
    print('lat: ', lat)
    print('lat type: ', type(lat))

    # regex to pull longitude line from log
    longireg = r'\'longitude\':\s\d{1,3}.\d{1,4},' 
    # pull longitude line from log
    longiLine = re.findall(longireg, log)
    print('longiLine: ', longiLine)
    print('longiLine type: ', type(longiLine))
    # convert longitude line to string
    longiLineStr = ' '.join([str(elem) for elem in longiLine])
    print('longiLineStr: ', longiLineStr)
    print('longiLineStr type: ', type(longiLineStr))

    # pull longitude only from longitude line
    longiList = re.findall(numsOnlyReg, longiLineStr)
    longi = ' '.join([str(elem) for elem in longiList])
    print('longi: ', longi)
    print('longi type: ', type(longi))

    # and now put it all into a dict to convert to json later
    pools = {} # dict
    pools['pool'] = []
    pools['pool'].append({
        'name': '',
        'ticker': '',
        'website': '',
        'node-id': '',
        'ip': ip,
        'latitude': lat,
        'longitude': longi,
        })

    print(pools)

       # latlong.write('\n'.join(latline))
       
