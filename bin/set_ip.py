#!/usr/bin/python
import os
import sys
from httplib import HTTPConnection
place = sys.argv[1]
password = sys.argv[2]
server = "go.xiaoyezi.org"

conn = HTTPConnection(server, 80)

conn.request("GET", "/ip")
response = conn.getresponse()
if response.status == 200:
    ip = response.read()
    conn.request("GET", "/ipset/%s/%s/%s" % (place, ip, password))
    r = conn.getresponse()
    print(r.read())
