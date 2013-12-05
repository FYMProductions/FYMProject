#! /usr/bin/python 

from socket import *

port = 5006
fileName = 'testing.txt'

class Server:
    gate = socket(AF_INET, SOCK_STREAM)   
    host = '127.0.0.1'

    def __init__(self, port):
    	self.fileName = fileName
        self.port = port
        self.gate.bind((self.host, self.port))  
        self.dolisten()

    def dolisten(self):
        self.gate.listen(10)
        while True:
            print("Listening for connections, on PORT: ", self.port)
            conn,address = self.gate.accept()
            #self.receiveFileName(conn)
            self.receiveFile(conn)


    def receiveFileName(self, sock):
        while True:
            data = sock.recv(1024)
            if len(data) > 0: 
            	print data
            self.fileName = data

    def receiveFile(self, sock):
        createFile = open("new_"+self.fileName, "wb")
        while True:
            data = sock.recv(1024)
            print data

            if data == "EOF\n":
            	break

            createFile.write(data)
        createFile.close()

server = Server(port)
