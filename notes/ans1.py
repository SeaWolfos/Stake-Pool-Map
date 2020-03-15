#!/usr/bin/env python
#this doesn't work. finding a different way
import asn1

with open('ip-asn.txt') as f:
    asn = f.read()
    decoder = asn1.Decoder()
    decoder.start(asn)
    tag, value = decoder.read()
    print(tag + ' ' + value)
