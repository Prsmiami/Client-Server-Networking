import socket
import datetime


def loopRecv(csoc, size):
    data = bytearray(b" "*size)
    mv = memoryview(data)
    while size:
        rsize = csoc.recv_into(mv,size)
        mv = mv[rsize:]
        size -= rsize
    return data


def Application(csoc, alias):
    size = 1000
    while (size > 999):
        rawmessage = input()
        if(rawmessage == "leave"):
            exit()
        message = str(datetime.datetime.now())[11:-7]
        message += "#"
        message += alias
        message += "#"
        message += rawmessage
        size = len(message)
        if(size > 999):
            print("message too large")

    # make sure size is 4 bytes
    if(size > 99): size = (str(size),":")
    elif(size > 9): size = ("0",str(size),":")
    else: size = ("00",str(size),":")

    # send size to server
    for e in size:
        csoc.sendall(e.encode("utf-8"))
    #csoc.sendall(size.encode())

    # send message to server
    for e in message:
        csoc.sendall(e.encode("utf-8"))
    #csoc.sendall(message.encode())
     
##    # recv 4 bytes from the server
##    data = int(loopRecv(csoc,4).decode()[:-1]) + 1
##
##    # recv size bytes from the server
##    data = loopRecv(csoc,data-1).decode()
##
##    messagelen = 0
##    for letter in data:
##        if(letter == '#'): break
##        else : messagelen += 1
##
##    #store time
##    time = data[:messagelen]
##    message = data[messagelen+1:]
##
##    messagelen = 0
##    for letter in message:
##        if(letter == '#'): break
##        else : messagelen += 1
##
##    #store alias
##    alias = message[:messagelen]
##
##    #store message
##    message = message[messagelen+1:]
##    print(time," ",alias,": ",message)

##                # recv 4 bytes from the client
##        size = loopRecv(csoc,4).decode()
##        loopbacksize = size
##        size = str(size)
##
##        #cut off delineator from size
##        size = (size)[:-1]
##        size = int(size)
##    
##        # recv (size) bytes from client
##        initmessage = loopRecv(csoc,size).decode()
##        initmessage = str(initmessage)
##
##        messagelen = 0
##        for letter in initmessage:
##            if(letter == '#'): break
##            else : messagelen += 1
##
##        #store time
##        time = initmessage[:messagelen]
##        message = initmessage[messagelen+1:]
##
##        messagelen = 0
##        for letter in message:
##            if(letter == '#'): break
##            else : messagelen += 1
##    
##        #store alias
##        alias = message[:messagelen]
##        #store message
##        message = message[messagelen+1:]
##
##        if(message == "leave"):
##            exit()
##
##        #temp = str(datetime.datetime.now())[11:-7]
##    
##        #display chat
##        print(time," ",alias,": ",message)
##
##        csoc.sendall(loopbacksize.encode("utf-8"))
##
##        for e in initmessage:
##            csoc.sendall(e.encode("utf-8"))
    

if __name__ == "__main__":
    # create the socket
    #  defaults family=AF_INET, type=SOCK_STREAM, proto=0, filno=None
    commsoc = socket.socket()
    
    # connect to localhost:5000
    commsoc.connect(("localhost",50000))

    print("Started Application")
    print("Please do not use the '#' value in your message or alias")
    print("Please enter your name")

    alias = input()

    print("You may begin writing messages.")
    
    # run the application protocol
    while True:
        Application(commsoc,alias)
    
    # close the comm socket
    commsoc.close()
