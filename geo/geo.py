#!/usr/bin/env python

from ipdata import ipdata
from pprint import pprint

f = open('/home/cam/projects/project_secrets/geo.key', 'r')
#print(f) # debugging#don't print API keys
apiKey = f.readline().strip() # strips away \n at EOL
ipdata = ipdata.IPData(apiKey) # api key goes here
#ipdata = ipdata.IPData('') #api key
with open('/home/cam/projects/Stake-Pool-Map/getIP/iplog.txt') as g:
    ip = g.readline().strip()
    print('ip: ', ip)
    response = ipdata.lookup(ip) #ip address - this will be !manual later
    pprint(response)
    with open("geoResponse.txt", "a") as h:
        h.write('\n'.join(response))


#status: only runs one IP, doesn't print the correct data to the file

# next steps: 
# 1. feed in many IP addresses 
# 2. suck lat/long from json response
    # see latlong.py


# 3. make new json with IP, node_id, lat, long
# 4. remove duplicate IPs, node_ids
# note: multiple IP addresses allowed per node? better include an add date in the json
# is postgres better at this point?
# 5. ?? not sure how to get pool ticker, name, website from node_id seeing as they don't match
# maybe one of the Cardano devs will respond if I reach out
# 6+. read from json/sql lat/long, put it on a map on a website
