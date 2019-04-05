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
                if(values[z] == '1'):           ##player 1 #or values[z] == '3'
                    stddraw.setPenColor(stddraw.BLUE)
                    stddraw.filledCircle(j + .5, i + .5, .25)
                elif(values[z] == '2'):         ##player 2
                    stddraw.setPenColor(stddraw.WHITE)
                    stddraw.filledCircle(j + .5, i + .5, .25)
                elif(values[z] == '3'):         ##player 1 king
                    stddraw.setPenColor(stddraw.WHITE)
                    stddraw.filledCircle(j + .5, i + .5, .25)
                    stddraw.setPenColor(stddraw.BLACK)
                    stddraw.text(j+.5, i+.5, "K")
                elif(values[z] == '4'):         ##player 2 king
                    stddraw.setPenColor(stddraw.WHITE)
                    stddraw.filledCircle(j + .5, i + .5, .25)
                    stddraw.setPenColor(stddraw.BLACK)
                    stddraw.text(j+.5, i+.5, "K")
                z+=1
    stddraw.show(500)
    

def loopRecv(csoc, size):
    data = bytearray(b" "*size)
    mv = memoryview(data)
    while size:
        rsize = csoc.recv_into(mv,size)
        mv = mv[rsize:]
        size -= rsize
    return data

def inbounds(move):
    rows="ABCDEFGH"
    cols="12345678"
    startindex=0
    destindex=0
    m0 = False
    m1 = False
    m2 = False
    m3 = False
    total = False
    for i in range(8):
        if(move[0] == rows[i]):
            startindex += 8*(i)
            m0 = True
        if(move[1] == cols[i]):
            startindex += (i)
            m1 = True
        if(move[2] == rows[i]):
            destindex += 8*(i)
            m2 = True
        if(move[3] == cols[i]):
            destindex += (i)
            m3 = True
    total = m0 and m1 and m2 and m3
    valid = total
    return valid

def inputDoubleJump(csoc,oldmove):
    flag=0
    while(flag==0):
        print("You can make another jump with the same piece, what do you request as the new destination(only type the destination)?")
        move = input()
        while (len(move) != 2 and abs (ord(oldmove[2]) - ord(move[0])) ==2):
            print("Please enter a valid 2 character jump move in the form of \n[nextrow][nextcolumn] \nfor example: D2")
            move = input()
        #sends a move of valid size to server to check if move is valid
        print("sending correct sized move to check for validity")
        fullmove = oldmove[2] + oldmove[3] + move
        print(fullmove)
        commsoc.sendall((fullmove).encode("utf-8"));
        print("move2 sent to server, now wait for server to respond...")
        isValid = loopRecv(csoc,1).decode()
        print("server sent back for isValid  ",isValid)
        if(isValid == 'I'):
            print("move invalid, terrible job")
            flag=0
        elif(isValid == 'V'):
            print("move valid! good job")
            flag=1
        elif(isValid == 'A'):   #you made a jump, maybe go again
            print("you jumped a piece! good job")
            flag=1

def inputmove(csoc,board):
    flag=0
    while(flag==0):
        move = input()

        #debug, print list of valid moves
        #print(validmoves(move,board))
        
        while ((len(move) != 4) or not(inbounds(move))):
            if(len(move) != 4):
                print("Please enter a valid 4 character move in the form of \n[currentrow][currentcolumn][nextrow][nextcolumn] \nfor example: C1D2")
            if(not(inbounds(move))):
                print("Locations must be between rows A and H, and columns 1 and 8")
            move = input()
        #sends a move of valid size to server to check if move is valid
        print("sending correct sized move to check for validity")
        commsoc.sendall((move).encode("utf-8"));
        print("move sent to server, now wait for server to respond...")
        isValid = loopRecv(csoc,1).decode()
        print("server sent response ",isValid)
        if(isValid == 'I'):
            print("move invalid, terrible job")
            flag=0
        elif(isValid == 'V'):
            print("move valid! good job")
            flag=1
        elif(isValid == 'A'):
            print("you're in position to make a double jump!!!")
            turn = loopRecv(csoc,1).decode()
            print(turn)
            board = loopRecv(csoc,32).decode()
            printcheckboard(board)
            print("do you want to make another move? yes/no")
            confirmation = input()
            if( confirmation == "y" or confirmation == "Y" or confirmation == "yes" or confirmation == "Yes"):
                
                inputDoubleJump(csoc,move)
            flag=1
        

def Application(csoc):
    startBoard='11111111111100000000222222222222'   #base start board
    print(loopRecv(csoc,8).decode())    #print which socket this client is
    while (True):
        turn = loopRecv(csoc,1).decode()
        print(turn)
        board = loopRecv(csoc,32).decode()
        print(board)
        printcheckboard(board)
        if(turn=="T"):          #if Turn, send 4 char move to server
            inputmove(csoc,board)
    
            
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
