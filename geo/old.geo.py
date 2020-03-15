#!/usr/bin/env python

from ipdata import ipdata
from pprint import pprint

f = open('/home/cam/projects/project_secrets/geo.key', 'r')
#print(f) # debugging#don't print API keys
apiKey = f.readline().strip() # strips away \n at EOL
ipdata = ipdata.IPData(apiKey) # api key goes here
#ipdata = ipdata.IPData('') #api key
response = ipdata.lookup('173.212.246.91') #ip address - this will be !manual later
pprint(response)
