import socket
import nmap

def printSSL():
    host = 'yahoo.com'
    addrs = socket.gethostbyname(host)
    #print (" Host is: ", host)

    nm = nmap.PortScanner()
    nm.scan(hosts= addrs, arguments='-n -sV --script ssl-enum-ciphers -Pn -p 443')
    ssl = nm[addrs]['tcp'][443]['script']['ssl-enum-ciphers']

    for item in ssl.split("\n"):
        if "TLSv" in item:
             version = item.strip()
             print ("SSL/TLS Version of " + str(host) + " is %s" % version)