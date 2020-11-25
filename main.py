from portforwarder import PortForwarder
import asyncore
import socket
import sys

if __name__ == "__main__":
    try:
        print("PYTHON PORT FORWARDER.....")
        lhost=str(input("LHOST>>"))
        lport=int(input("LPORT>>"))
        rhost=str(input("RHOST>>"))
        rport=int(input("RPORT>>"))
        '''
        lhost="127.0.0.1"
        lport=8888
        rhost="127.0.0.1"
        rport=80
        #simply forwarding to localhost:80 to check
        '''
        PortForwarder(lhost,lport,rhost,rport)
        asyncore.loop()
    except KeyboardInterrupt:
        print("INTERRUPTED >>> BYE!")
        sys.exit()
