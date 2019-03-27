import selectors
import socket
import threading

class waitinguser:
    socket = 0
    roomcode = 0  

    

    def make_waitinguser(var1,var2):
        socket = var1
        roomcode = var2

def doAccept(thesel, thesock, mask):
    # accept the connection
    commsoc, raddr = thesock.accept()
    print("Connection from:", raddr)
    # set non-blocking
    commsoc.setblocking(False)
    # register
    thesel.register(commsoc, selectors.EVENT_READ, doRead)

def Roomhandler(sock1, sock2, mask):
    
    ##insert function here
    sock1.sendall(("socket 1").encode("utf-8"))
    sock2.sendall(("socket 2").encode("utf-8"))
    

def doRead(thesel, thesock, mask):
    data = thesock.recv(1)
    global randomflag
    global randomopponent
    global waitlist
    deleteflag = 0
    if data:
        print("recv:", data)

    ##code for random room    
        if(data.decode() == 'R'):
            if(randomflag == 0):
                randomopponent = thesock
                randomflag = 1
            else:
                t1 = threading.Thread(name="first", target=Roomhandler, args=(randomopponent,thesock,mask))
                t1.start()
                thesel.unregister(randomopponent)
                thesel.unregister(thesock)

    ##code for specified room number
        if(data.decode() == 'C'):
            data = (thesock.recv(6)).decode()
            print("Room number: ",data)
            for e in waitlist:
                if(waitlist[e].roomcode == data):
                    t1 = threading.Thread(name="first", target=Roomhandler, args=(e.socket,thesock,mask))
                    t1.start()
                    thesel.unregister(e.sock)
                    thesel.unregister(thesock)
                    delindex = e
                    deleteflag = 1
                    break
            if(deleteflag == 1):
                del waitlist[delindex]
            else:
                i = len(waitlist)
                waitlist[i] = waitinguser.make_waitinguser(thesock,data)


if __name__ == "__main__":

    randomflag = 0
    threadnum = 0
    randomopponent = 0
    waitlist = [100]
    
    # create the selector
    sel = selectors.DefaultSelector()
    
    # create the server socket
    #  defaults family=AF_INET, type=SOCK_STREAM, proto=0, filno=None
    serversoc = socket.socket()
    
    # make is non blocking
    serversoc.setblocking(False)
    
    # bind to local host:5000
    serversoc.bind(("localhost",50000))
                   
    # make passive with backlog=10
    serversoc.listen(10)
    
    # register the server socket
    sel.register(serversoc, selectors.EVENT_READ, doAccept)
    
    # wait for incoming connections
    while True:
        
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(sel, key.fileobj, mask)
        

    
    # close the server socket
    serversoc.close()
