import socket
import datetime
import stddraw
import sys

def f(x):   #dictionary for what color circle will be drawn over black square
    return {
        1: 'WHITE',
        2: 'RED'
    }.get(x, 'BLACK')   #default is black, so nothing shows if values[z]=0

def printcheckboard(values): 
    n = 8
    stddraw.setXscale(0, n)
    stddraw.setYscale(0, n)
    z = 0 ##z is the spot in values array
        
    for i in range(n):
        for j in range(n):
            if ((i + j) % 2) != 0:
                stddraw.setPenColor(stddraw.BLACK)
            else:
                stddraw.setPenColor(stddraw.RED)
            stddraw.filledSquare(i + .5, j + .5, .5)
            if(stddraw.getPenColor() == 'BLACK'):
                stddraw.setPenColor( f(values[z]) )
                stddraw.filledCircle(i + .5, j + .5, .25)
                z+=1
    stddraw.show()
  

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
    # driver code 
    printcheckboard() 
    
    


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
