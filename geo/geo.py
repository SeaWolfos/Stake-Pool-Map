#!/usr/bin/env python

from ipdata import ipdata
from pprint import pprint

f = open('/home/cam/projects/project_secrets/ipdata.co.key')
print(f)
apiKey = f.readline().strip()
ipdata = ipdata.IPData(apiKey) #api key
#ipdata = ipdata.IPData('') #api key
response = ipdata.lookup('173.212.246.91') #ip address
pprint(response)
