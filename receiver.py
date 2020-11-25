import socket
import asyncore

class receiver(asyncore.dispatcher):
    def __init__(self,conn):
        asyncore.dispatcher.__init__(self,conn)
        self.frombuff=b''
        self.tobuff=b''
        #should be always in bytes or error will come
        self.sender=None

    def handle_connect(self):
        pass

    def handle_read(self):
        read = self.recv(4096)
        self.frombuff += read

    def writable(self):
        return (len(self.tobuff) > 0)

    def handle_write(self):
        sent = self.send(self.tobuff)
        self.tobuff = self.tobuff[sent:]

    def handle_close(self):
        self.close()
        if self.sender:
            self.sender.close()