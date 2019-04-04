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
            if((i + j) % 2) == 0:
                if(values[z] == '1'):           ##player 1
                    stddraw.setPenColor(stddraw.BLUE)
                elif(values[z] == '2'):         ##player 2
                    stddraw.setPenColor(stddraw.WHITE)
                stddraw.filledCircle(j + .5, i + .5, .25)
                z+=1
    stddraw.show()

def isvalid(board, move):

    difference = 0

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
