import socket

def loopRecv(csoc, size):
    data = bytearray(b" "*size)
    mv = memoryview(data)
    while size:
        rsize = csoc.recv_into(mv,size)
        mv = mv[rsize:]
        size -= rsize
    return data


def baseTCPProtocolC(csoc):
    print("Started baseTCPProtocol")
        
    # send 10 bytes to client
    mess = "1234567890"
    csoc.sendall(mess.encode("utf-8"))
    
    # recv 10 bytes from the client
    data = loopRecv(csoc,10)

    print("Ended baseTCPProtocol")
    

if __name__ == "__main__":
    # create the socket
    #  defaults family=AF_INET, type=SOCK_STREAM, proto=0, filno=None
    commsoc = socket.socket()
    
    # connect to localhost:5000
    commsoc.connect(("localhost",55005))
    
    # run the application protocol
    baseTCPProtocolC(commsoc)
    
    # close the comm socket
    commsoc.close()

    
