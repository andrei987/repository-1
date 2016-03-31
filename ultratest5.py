#! python

import socket # for socket
import sys 
import datetime

t = datetime.datetime.now()
print "current time is: ", t


list = ['www.wikipedia.com' , 'www.google.ro' , 'www.yahoo.com' , 'https://github.com/andrei987/repository-1/blob/master/ultratest2_server.py']
port = 80

for i in list:
    try:
    	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	print "Socket successfully created"
    except socket.error as err:
    	print "socket creation failed with error %s" %(err)


    try:
        host_ip = socket.gethostbyname(i)

    except socket.gaierror:
    #this means could not resolve the host
    	print "there was an error resolving the host", i
    	sys.exit()

    # connecting to the server
    s.connect((host_ip,port))

    print "the socket has successfully connected to",  i, " on port == %s" %(host_ip)
    
