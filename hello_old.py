#!/usr/bin/env python

import socket
import re

host = ''
port = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

def extractIP( ipStr):
    l = re.split('(\d{,3}\.\d{,3}\.\d{,3})\.(\d{,3})', ipStr)
    return l[1:-1]

# Loop forever, listening for requests:
while True:
    csock, caddr = sock.accept()
    print ("Connection from: " + repr(caddr[0]))
    req = csock.recv(1024) # get the request, 1kB max
    print (req)
    con_ip= extractIP(repr(caddr[0]))
    print ("last octet:", con_ip[1])
    logline="Request:"+str(req)+" From: "+repr(caddr)
    if (int(con_ip[1]) % 2 == 0):
        f = open("/tmp/odd.log","w")
        f.write(logline)
        f.close()
        print ("even")
    else:
        f = open("/tmp/odd.log", "w")
        f.write(logline)
        f.close()
        print ("odd")

    match = re.match(b'GET / HTTP/1.(\d+)\s', req)
    if match:
        print ("GET request is Ok! \n")
        csock.sendall(b"""HTTP/1.0 200 OK
Content-Type: text/html

<html>
<head>
<title>Hi there!!</title>
</head>
<body>
Hi there!!
</body>
</html>
""")
    else:
        print ("Returning 404")
        csock.sendall(b"HTTP/1.0 404 Not Found\r\n")
    csock.close()
