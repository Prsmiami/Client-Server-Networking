import selectors
import socket
import threading

def loopRecv(csoc, size):
    data = bytearray(b" "*size)
    mv = memoryview(data)
    while size:
        rsize = csoc.recv_into(mv,size)
        mv = mv[rsize:]
        size -= rsize
    return data

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

def doAccept(thesel, thesock, mask):
    # accept the connection
    commsoc, raddr = thesock.accept()
    print("Connection from:", raddr)
    # set non-blocking
    commsoc.setblocking(False)
    # register
    thesel.register(commsoc, selectors.EVENT_READ, doRead)

def endgamecheck(board):
    p1flag = 0
    p2flag = 0
    for e in board:
        if(
    for e in board:
        if(
    for e in board:
        if(
    for e in board:

def Roomhandler(sock1, sock2, mask):

    sock1.setblocking(True)
    sock2.setblocking(True)
    sock1.sendall(("socket 1").encode("utf-8"))
    sock2.sendall(("socket 2").encode("utf-8"))
##  turn 1 is for socket 1
    turn = 1
    endgame = 0
    mult = 0
    base = 0
    fromindex = 0
    toindex = 0
    difference = 0
    move = ""
    board = [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2]
    while(endgame != 1):
        if(turn == 1):
            sock1.sendall(('T').encode("utf-8"))
            sock2.sendall(('N').encode("utf-8"))
            for e in board:
                sock1.sendall(str(e).encode("utf-8"))
                sock2.sendall(str(e).encode("utf-8"))
            move = (loopRecv(sock1,4)).decode()
            if(move[0] == 'A'):
                mult = 0
            elif (move[0] == 'B'):
                mult = 1
            elif(move[0] == 'C'):
                mult = 2
            elif(move[0] == 'D'):
                mult = 3
            elif(move[0] == 'E'):
                mult = 4
            elif(move[0] == 'F'):
                mult = 5
            elif(move[0] == 'G'):
                mult = 6
            elif(move[0] == 'H'):
                mult = 7
            if(move[1] == '1'):
                base = 0
            elif(move[1] == '2'):
                base = 0
            elif(move[1] == '3'):
                base = 1
            elif(move[1] == '4'):
                base = 1
            elif(move[1] == '5'):
                base = 2
            elif(move[1] == '6'):
                base = 2
            elif(move[1] == '7'):
                base = 3
            elif(move[1] == '8'):
                base = 3
            fromindex = base + (mult*4)

            if(move[2] == 'A'):
                mult = 0
            elif(move[2] == 'B'):
                mult = 1
            elif(move[2] == 'C'):
                mult = 2
            elif(move[2] == 'D'):
                mult = 3
            elif(move[2] == 'E'):
                mult = 4
            elif(move[2] == 'F'):
                mult = 5
            elif(move[2] == 'G'):
                mult = 6
            elif(move[2] == 'H'):
                mult = 7
            if(move[3] == '1'):
                base = 0
            elif(move[3] == '2'):
                base = 0
            elif(move[3] == '3'):
                base = 1
            elif(move[3] == '4'):
                base = 1
            elif(move[3] == '5'):
                base = 2
            elif(move[3] == '6'):
                base = 2
            elif(move[3] == '7'):
                base = 3
            elif(move[3] == '8'):
                base = 3
            toindex = base + (mult*4)               


            if((move[0] == (move[2]-1)) and move[0] != H):
                if(board[fromindex] == 1):
                    if(board[toindex] == 0):
                        board[fromindex] = 0
                        board[toindex] = 1
                        sock1.sendall(("V").encode("utf-8"))
                    else:
                        print("Please select a space that is not occupied by another piece.")
                        sock1.sendall(("I").encode("utf-8"))
                else:
                    print("Please select a piece that is yours. Your pieces are on the bottom.")
                    sock1.sendall(("I").encode("utf-8"))
            elif((move[0] == (move[2]-2)) and (move[0] != H) and (move[0] != G)):
                if(board[fromindex] == 1):
                    difference = toindex-fromindex
                    if(difference == 10):
                        if(board[fromindex+4] == 2):
                            board[fromindex+4] = 0
                            board[fromindex] = 0
                            board[toindex] = 1
                            sock1.sendall(("V").encode("utf-8"))
                    elif(difference == 7):
                        if(board[fromindex+3] == 2):
                            board[fromindex+4] = 0
                            board[fromindex] = 0
                            board[toindex] = 1
                            sock1.sendall(("V").encode("utf-8"))
                    else:
                        print("Invalid move")
                        sock1.sendall(("I").encode("utf-8"))
                else:
                    print("Please select a piece that is yours. Your pieces are on the bottom")
                    sock1.sendall(("I").encode("utf-8"))

            
        if(turn == 2):
            sock2.sendall(("T").encode("utf-8"))
            sock1.sendall(("N").encode("utf-8"))
            for e in board:
                sock1.sendall((e).encode("utf-8"))
                sock2.sendall((e).encode("utf-8"))
            move = (loopRecv(sock1,4)).decode()
            if(move[0] == 'A'):
                mult = 0
            elif(move[0] == 'B'):
                mult = 1
            elif(move[0] == 'C'):
                mult = 2
            elif(move[0] == 'D'):
                mult = 3
            elif(move[0] == 'E'):
                mult = 4
            elif(move[0] == 'F'):
                mult = 5
            elif(move[0] == 'G'):
                mult = 6
            elif(move[0] == 'H'):
                mult = 7
            if(move[1] == '1'):
                base = 0
            elif(move[1] == '2'):
                base = 0
            elif(move[1] == '3'):
                base = 1
            elif(move[1] == '4'):
                base = 1
            elif(move[1] == '5'):
                base = 2
            elif(move[1] == '6'):
                base = 2
            elif(move[1] == '7'):
                base = 3
            elif(move[1] == '8'):
                base = 3
            fromindex = base + (mult*4)

            if(move[2] == 'A'):
                mult = 0
            elif(move[2] == 'B'):
                mult = 1
            elif(move[2] == 'C'):
                mult = 2
            elif(move[2] == 'D'):
                mult = 3
            elif(move[2] == 'E'):
                mult = 4
            elif(move[2] == 'F'):
                mult = 5
            elif(move[2] == 'G'):
                mult = 6
            elif(move[2] == 'H'):
                mult = 7
            if(move[3] == '1'):
                base = 0
            elif(move[3] == '2'):
                base = 0
            elif(move[3] == '3'):
                base = 1
            elif(move[3] == '4'):
                base = 1
            elif(move[3] == '5'):
                base = 2
            elif(move[3] == '6'):
                base = 2
            elif(move[3] == '7'):
                base = 3
            elif(move[3] == '8'):
                base = 3
            toindex = base + (mult*4)

##        if((move[0] == (move[2]-1)) and move[0] != H):
##            if(board[fromindex] == 1):
##                if(board[toindex] == 0):
##                    board[fromindex] = 0
##                    board[toindex] = 1
##                else: print("Please select a space that is not occupied by another piece.")
##            else: print("Please select a piece that is yours. Your pieces are on the bottom.")
##        elif((move[0] == (move[2]-2)) and (move[0] != H) and (move[0] != G)):
##            if(board[fromindex] == 1):
##                difference = 0
##                
##                if(board[toindex] == 0):
##                    if(
##                    else(
##
##            else: print("Please select a piece that is yours. Your pieces are on the bottom")
        
    

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
