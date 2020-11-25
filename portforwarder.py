import socket
import asyncore
from sender import sender
from receiver import receiver

class PortForwarder(asyncore.dispatcher):
    def __init__(self,ip,port,remoteip,remoteport):
        asyncore.dispatcher.__init__(self)
        self.remoteip=remoteip
        self.remoteport=remoteport
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((ip,port))
        self.listen(5)

    def handle_accept(self):
        conn , addr = self.accept()
        print("CONNECTED ON LOCAL %s : %s"%(addr[0],addr[1]))
        sender(receiver(conn),self.remoteip,self.remoteport)
