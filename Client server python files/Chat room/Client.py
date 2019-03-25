import socket
import datetime
import threading
import time

def loopRecv(csoc, size):
    data = bytearray(b" "*size)
    mv = memoryview(data)
    while size:
        rsize = csoc.recv_into(mv,size)
        mv = mv[rsize:]
        size -= rsize
    return data


def Application():

    # create the socket
    #  defaults family=AF_INET, type=SOCK_STREAM, proto=0, filno=None
    csoc = socket.socket()
    
    # connect to localhost:5000
    csoc.connect(("localhost",50000))

    print("Started Application")
    print("Please do not use the '#' value in your message or alias")
    print("Please enter your name")

    alias = input()

    print("You may begin writing messages.")

    while True:
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
        ''.join(message)

##        # make sure size is 4 bytes
##        if(size > 99): size = (str(size),":")
##        elif(size > 9): size = ("0",str(size),":")
##        else: size = ("00",str(size),":")

        # send message to server
        csoc.sendall(message.encode("utf-8"))
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

    csoc.close()
    return

def myThread2():
    print("Started thread ", threading.current_thread())

    mc_addr = "224.0.0.70"
    mc_port = 50000
    soc = socket.socket(type=socket.SOCK_DGRAM)

    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    soc.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)
    soc.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)

    soc.bind(("",mc_port))
    lhost = socket.gethostbyname("localhost");
    soc.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton(lhost))

    soc.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(mc_addr) + socket.inet_aton(lhost))


    while True:
        data, addr = soc.recvfrom(256)
        data = data.decode()
    
        initmessage = str(data)

        messagelen = 0
        for letter in initmessage:
            if(letter == '#'): break
            else : messagelen += 1

        #store time
        time = initmessage[:messagelen]
        print(time)
        message = initmessage[messagelen+1:]


        messagelen = 0
        for letter in message:
            if(letter == '#'): break
            else : messagelen += 1
    
        #store alias
        alias = message[:messagelen]
        print(alias)
        #store message
        message = message[messagelen+1:]
        print(message)

        if(message == "leave"):
            exit()

        #temp = str(datetime.datetime.now())[11:-7]
    
        #display chat
        print(time," ",alias,": ",message)

    print("Ending thread ", threading.current_thread())
    return


if __name__ == "__main__":


    # create thread 1, no arguments
    t1 = threading.Thread(name="first", target=Application)
    
    # create thread 2, 1 argument
    t2 = threading.Thread(name="second", target=myThread2)
    
    # start threads
    t2.start()
    t1.start()


##    # run the application protocol
##    while True:
##        Application(commsoc,alias)
    
    # close the comm socket

