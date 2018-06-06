# dnsextractor
Extracción de información en servidores DNS con Python

Query Type | Comments
------------ | -------------
A | IPv4
AAAA | IPv6
MX | MailServers
NS | NameServers


**Usage:** python dnsextractor.py [domain] [querytype]

**Example:** python dnsextractor.py github.com NS
