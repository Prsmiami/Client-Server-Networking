import socket

def loopRecv(csoc, size):
    data = bytearray(b" "*size)
    mv = memoryview(data)
    while size:
        rsize = csoc.recv_into(mv,size)
        mv = mv[rsize:]
        size -= rsize
    return data


def baseTCPProtocolS(csoc):
    print("Started baseTCPProtocol")
    
    # recv 10 bytes from the client
    data = loopRecv(csoc,10)
    
    # send 10 bytes to client
    csoc.sendall(data)
    
    print("Ended baseTCPProtocol")
    


if __name__ == "__main__":
    # create the server socket
    #  defaults family=AF_INET, type=SOCK_STREAM, proto=0, filno=None
    serversoc = socket.socket()
    
    # bind to local host:5000
    serversoc.bind(("localhost",55005))
                   
    # make passive with backlog=5
    serversoc.listen(5)
    
    # wait for incoming connections
    while True:
        print("Listening on ", 55005)
        
        # accept the connection
        commsoc, raddr = serversoc.accept()
        
        # run the application protocol
        baseTCPProtocolS(commsoc)
        
        
        # close the comm socket
        commsoc.close()
    
    # close the server socket
    serversoc.close()
    
