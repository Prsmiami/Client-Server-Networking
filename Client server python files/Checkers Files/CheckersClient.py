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

    print(loopRecv(csoc,8).decode())
    


if __name__ == "__main__":
    # create the socket
    #  defaults family=AF_INET, type=SOCK_STREAM, proto=0, filno=None
    commsoc = socket.socket()
    
    # connect to localhost:5000
    commsoc.connect(("localhost",50000))

    print("Started Application")

    while(True):
        print("Please type either 'random' for a random opponent or a 6 digit alphanumeric room code for a match with a friend.")
        roomtype = ""
        roomtype = input()

        print("You typed: ",roomtype,", is this correct?");
        confirmation = input();
        if(len(roomtype) == 6):
            if( confirmation == "y" or confirmation == "Y" or confirmation == "yes" or confirmation == "Yes"): break
        else: print("Must enter either 'random' or a 6 digit alphanumeric code")

    if(roomtype == "random" or roomtype == "Random"):
        commsoc.sendall(("R").encode("utf-8"));
    else:
        commsoc.sendall(("C").encode("utf-8"));
        commsoc.sendall((roomtype).encode("utf-8"));
    
    # run the application protocol    
    Application(commsoc)
    
    # close the comm socket
    commsoc.close()
