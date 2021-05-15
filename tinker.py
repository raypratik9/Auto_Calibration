import socket
import sys
import time
global value
import tkinter as tk
from t import data
value=0
if __name__ == '__main__':
    print(value)
    value=data()
    print(value)
    try:
        s = socket.socket()#socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket successfully created")
    except socket.error as err:
        print ("Socket creation failed %s" %(err))
    port = 8080

    try:
        host_ip = socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        print("There was a error")
        sys.exit();
    s.bind((host_ip,port))
    print(host_ip);

    s.listen(5)
    print("listening")
    Server1, addr1 = s.accept()      
    print ('Got connection from', addr1)
    #Server2, addr2 = s.accept()      
    #print ('Got connection from', addr2)
