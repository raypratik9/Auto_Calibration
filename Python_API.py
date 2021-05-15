import socket
import sys
import time
from flask import render_template,Flask,request
global value
app = Flask(__name__)

def client_data(value):
    mystring=str(value)+'*'
    b = bytes(mystring, 'utf-8')
    Server1.send(b)
    print("data from client:")
    print(Server1.recv(1024))
        
@app.route("/", methods=["POST", "GET"])
def index():
    global value
    if request.method == "POST":
        value = request.form["value"]
        print(value)
        client_data(value)
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    global value
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
    app.run()
