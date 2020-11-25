import socket
import asyncore

class sender(asyncore.dispatcher):
    def __init__(self, receiver, remoteaddr,remoteport):
        asyncore.dispatcher.__init__(self)
        self.receiver=receiver
        receiver.sender=self
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((remoteaddr, remoteport))

    def handle_connect(self):
        pass

    def handle_read(self):
        read = self.recv(4096)
        self.receiver.tobuff += read

    def writable(self):
        return (len(self.receiver.frombuff) > 0)

    def handle_write(self):
        sent = self.send(self.receiver.frombuff)
        self.receiver.frombuff = self.receiver.frombuff[sent:]

    def handle_close(self):
        self.close()
        self.receiver.close()