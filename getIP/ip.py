#!/usr/bin/env python

# pulls IP addresses from logs
# BOOM BAM BABY IT WORKS

import re
reggie = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

#new.txt is an example of the logs
with open('../data/new.txt') as f:
    log = f.read()
    iplist = re.findall(reggie,log)
    with open("iplog.txt", "a") as iplog:
        iplog.write('\n'.join(iplist))

