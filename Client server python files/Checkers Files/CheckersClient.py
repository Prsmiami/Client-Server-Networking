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

def isvalid(move):

    if((move[0] == (move[2]-1)) and move[0] != H):
        if(board[fromindex] == 1):
            if(board[toindex] == 0):
                board[fromindex] = 0
                board[toindex] = 1
            else: print("Please select a space that is not occupied by another piece.")
        else: print("Please select a piece that is yours. Your pieces are on the bottom.")
    elif((move[0] == (move[2]-2)) and (move[0] != H) and (move[0] != G)):
        if(board[fromindex] == 1):
            difference = 0
            if(board[toindex] == 0):
                if(
                else(

        else: print("Please select a piece that is yours. Your pieces are on the bottom")
  

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

    ##for untouched board in start state vvv
    startBoard='11111111111100000000222222222222'
    print(loopRecv(csoc,8).decode())
    # driver code
    
    turn = loopRecv(csoc,1).decode()
    print(turn)

    board = loopRecv(csoc,32).decode()
    
    print(board)
    printcheckboard(board)
    isValid = 1;

    if(turn=='T')
        move = input()
        while ((len(move) != 4) || !(isValid))
            if(len(move) != 4)
                print("Please enter a valid 4 character move in the form of \n[currentrow][currentcolumn][nextrow][nextcolumn] \nfor example: C1D2")
            if(!(isValid))
                print("Please enter a valid move, your piece cant move there!"
    


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
