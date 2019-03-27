import selectors
import socket
import threading

class waitinguser:
    prevuser = 0
    socket = 0
    roomcode = 0
    nextuser = 0

def make_waitinguser(var1,var2):
    user = waitinguser()
    user.socket = var1
    user.roomcode = var2
    return user

def setnext(temp):
    nextuser = temp

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
    tempptr = waitlist
    followingptr = waitinguser()
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
            while(tempptr != 0):
                if(tempptr.roomcode == data):
                    t1 = threading.Thread(name="first", target=Roomhandler, args=(tempptr.socket,thesock,mask))
                    t1.start()
                    thesel.unregister(tempptr.socket)
                    thesel.unregister(thesock)
                    deleteflag = 1
                    break
                else:
                    followingptr = tempptr
                    tempptr = tempptr.nextuser
            if(deleteflag == 1):
                followingptr.nextuser = tempptr.nextuser
                del tempptr
            else:
                ##issue will be with this user being deleted at end of function
                newuser = make_waitinguser(thesock,data)
                followingptr.nextuser = newuser


if __name__ == "__main__":

    randomflag = 0
    threadnum = 0
    randomopponent = 0
    
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

    waitlist = make_waitinguser(serversoc,0)
    
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
