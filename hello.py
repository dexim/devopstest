from flask import Flask, request
import re,base64

app = Flask(__name__)

def extractIP(ipStr):
    l = re.split('(\d{,3}\.\d{,3}\.\d{,3})\.(\d{,3})', ipStr)
    return l[1:-1]

@app.route('/')

def hello_world():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    print ("IP:", ip)
    con_ip= extractIP(ip)
#    print ("last octet:", con_ip[1])
    r_headers =  str(request.headers)
    r_data= str(request.get_data().decode('utf-8'))
    logline="From: "+repr(ip)+" Headers:"+r_headers+" Data:"+r_data
    if (int(con_ip[1]) % 2 == 0):
        f = open("/tmp/even.log","a")
        f.write(logline)
        f.close()
#        print ("even")
    else:
        f = open("/tmp/odd.log", "a")
        f.write(logline)
        f.close()
#        print ("odd")

    return 'Hello, World!'

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)
