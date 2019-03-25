import selectors
import socket

def doAccept(thesel, thesock, mask):
    # accept the connection
    commsoc, raddr = thesock.accept()
    print("Connection from:", raddr)
    # set non-blocking
    commsoc.setblocking(False)
    # register
    thesel.register(commsoc, selectors.EVENT_READ, doRead)

def doRead(thesel, thesock, mask):
    data = thesock.recv(256)
    esoc = socket.socket(type=socket.SOCK_DGRAM)
    mc_addr = "224.0.0.70"
    mc_port = 50000
    esoc.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
    lhost = socket.gethostbyname("localhost")
    esoc.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(lhost))

    if data:
        print("recv:", data)
        esoc.sendto(data,(mc_addr, mc_port))
##    else:
##        print("closing", thesock)
##        thesel.unregister(thesock)
##        thesock.close()

if __name__ == "__main__":
    
    # create the selector
    sel = selectors.DefaultSelector()
    
    
    # create the server socket
    #  defaults family=AF_INET, type=SOCK_STREAM, proto=0, filno=None
    serversoc = socket.socket()
    
    # make is non blocking
    serversoc.setblocking(False)
    
    # bind to local host:5000
    serversoc.bind(("localhost",50000))
                   
    # make passive with backlog=5
    serversoc.listen(5)
    
    # register the server socket
    sel.register(serversoc, selectors.EVENT_READ, doAccept)
    
    # wait for incoming connections
    while True:
        print("Listening on ", 50000)
        
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(sel, key.fileobj, mask)
        

    
    # close the server socket
    serversoc.close()
