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
    z = 0 ##z is the spot in values string
    rows = 'ABCDEFGH'
    cols = '12345678'
        
    for i in range(n):
        for j in range(n): 
            if ((i + j) % 2) != 0:
                stddraw.setPenColor(stddraw.BLACK)
            else:
                stddraw.setPenColor(stddraw.RED)
            stddraw.filledSquare(j + .5, i + .5, .5)
            stddraw.setPenColor(stddraw.YELLOW)
            location = rows[i] + cols[j]
            stddraw.text(j+.15, i+.1, location)
            if((i + j) % 2) == 0:
                if(values[z] == '1'):           ##player 1
                    stddraw.setPenColor(stddraw.BLUE)
                    stddraw.filledCircle(j + .5, i + .5, .25)
                elif(values[z] == '2'):         ##player 2
                    stddraw.setPenColor(stddraw.WHITE)
                    stddraw.filledCircle(j + .5, i + .5, .25)
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

def inputmove():
        while(flag==0):
            move = input()
            while (len(move) != 4):
                print("Please enter a valid 4 character move in the form of \n[currentrow][currentcolumn][nextrow][nextcolumn] \nfor example: C1D2")
                move = input()
            #sends a move of valid size to server to check if move is valid
            print("sending correct sized move")
            commsoc.sendall((move).encode("utf-8"));
            isValid = loopRecv(csoc,1).decode()
            if(isValid == 'I'):
                flag=0
            elif(isValid == 'V'):
                flag=1

def Application(csoc):

    ##Recieve board
    ##Recieve turn code/endgame
    ##Input move or wait for recieve board

    ##for untouched board in start state vvv
    startBoard='11111111111100000000222222222222'

    print(loopRecv(csoc,8).decode())
    
    turn = loopRecv(csoc,1).decode()
    print(turn)
    board = loopRecv(csoc,32).decode()
    print(board)
    printcheckboard(board)
    
    #while !endgame for loops below

    
    if(turn=='T'):          #if Turn, send 4 char move to server
        inputmove()
        
    turn = loopRecv(csoc,1).decode()
    print(turn)
    board = loopRecv(csoc,32).decode()
    print(board)
    printcheckboard(board)
    
            
if __name__ == "__main__":
    # create the socket
    #  defaults family=AF_INET, type=SOCK_STREAM, proto=0, filno=None
    commsoc = socket.socket()
    
    # connect to localhost:5000
    commsoc.connect(("localhost",50000))

    print("Started Application")

##    while(True):
##        print("Please type either 'random' for a random opponent or a 6 digit alphanumeric room code for a match with a friend.")
##        roomtype = ""
##        roomtype = input()
##
##        print("You typed: ",roomtype,", is this correct?");
##        confirmation = input();
##        if(len(roomtype) == 6):
##            if( confirmation == "y" or confirmation == "Y" or confirmation == "yes" or confirmation == "Yes"): break
##        else: print("Must enter either 'random' or a 6 digit alphanumeric code")
##
##    if(roomtype == "random" or roomtype == "Random"):
##        commsoc.sendall(("R").encode("utf-8"));
##    else:
##        commsoc.sendall(("C").encode("utf-8"));
##        commsoc.sendall((roomtype).encode("utf-8"));

    commsoc.sendall(("R").encode("utf-8")); #auto random room

    
    # run the application protocol    
    Application(commsoc)
    
    # close the comm socket
    commsoc.close()
