#!/usr/bin/env python
# -*- coding utf-8 -*-

import dns.resolver
import sys

def dnsQuery(domain, lookuptype):
    try:
        answer = dns.resolver.query(domain,lookuptype)
        for ans in answer:
            if lookuptype == 'A' or lookuptype=='a':
                print('Domain: {} - DNS Lookuptype: {} - Answer: {}'.format(domain,lookuptype,ans.address))
            elif lookuptype == 'AAAA' or lookuptype=='aaaa':
                print('Domain: {} - DNS Lookuptype: {} - Answer: {}'.format(domain,lookuptype,ans.address))
            elif lookuptype == 'MX' or lookuptype=='mx':
                print('Domain: {} - DNS Lookuptype: {} - Answer: {} - Preference: {}'.format(domain,lookuptype,ans.exchange,ans.preference))
            elif lookuptype == 'NS' or lookuptype=='ns':
                print('Domain: {} - DNS Lookuptype: {} - Answer: {}'.format(domain,lookuptype,ans.target))
    except Exception as e:
            print(e)


def intel():
    archivo = open(sys.argv[1], 'r')
    for linea in archivo.readlines():
        dnsQuery(linea.replace('\n', ''), sys.argv[2])
        print('\n')
    archivo.close() 


if __name__ == '__main__':
    if len (sys.argv) != 3 :
        print("\nUsage: python dnsextractor.py [domain] [querytype]\n")
        print("\tQueryTypes: A(IPv4), AAAA(IPv6), MX(MailServers), NS(NameServers)\n")
        print("Example: python dnsextractor.py github.com NS\n")
        sys.exit (1)
    else:
        intel()