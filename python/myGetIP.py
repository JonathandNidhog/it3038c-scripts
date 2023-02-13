import socket, sys

#hostname =str(sys.argv[1])

#ip = socket.gethostbyname(hostname)
#print(hostname +' has an IP of ' + ip)


def getHostnameByIP(h):
    getHostnameByIP(sys.argv[1])
try:
    h = sys.argv[1]
    hostname = str(h)
    ip = socket.gethostbyname(hostname)
    print (hostname +' has an IP of ' + ip)

except:
    print("Oops, something is wrong with that host")