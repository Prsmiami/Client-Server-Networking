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


def Application(csoc):

    ##Recieve board
    ##Recieve turn code/endgame
    ##Input move or wait for recieve board
    ##


    
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
        

if __name__ == "__main__":
    # create the socket
    #  defaults family=AF_INET, type=SOCK_STREAM, proto=0, filno=None
    commsoc = socket.socket()
    
    # connect to localhost:5000
    commsoc.connect(("localhost",50000))

    print("Started Application")

    while(true):
        print("Please type either 'random' for a random opponent or a 6 digit alphanumeric room code for a match with a friend.")

        roomtype = input()

        print("You typed: ",roomtype," , is this correct?");
        confirmation = input();
        if(len(roomtype) = 6):
            if(confirmation = ("y" || "Y" || "yes" || "Yes"): break;
        else: print("Must enter either 'random' or a 6 digit alphanumeric code");

    if(roomtype = "random" || "Random"):
        csoc.sendall(("R").encode("utf-8"));
    else:
        csoc.sendall(("C").encode("utf-8"));
        csoc.sendall(roomtype);
    
    # run the application protocol    
    Application(commsoc)
    
    # close the comm socket
    commsoc.close()
