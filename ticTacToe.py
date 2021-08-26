#impact pygame
from array import *
# import random
import random

board = [
         [' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']
         ]

randomNumberList = [0,1,2]

#Checks if its the players turn
#def playerTurn(turn):
#    return turn%2 == 0

#enter selection
def enterMove():
    chosing = True
    userX = input("Enter your X: ")
    userY = input("Enter your Y: ")
    userX = int(userX)
    userY = int(userY)
    userInfo = [0] * 2
    while(chosing):
        if board[userX][userY] == ' ':
            board[userX][userY] = 'X'
            chosing = False
        else:
            userX = input("Enter your X again: ")
            userY = input("Enter your Y again: ")
            userX = int(userX)
            userY = int(userY)
            
    userInfo = [0] * 2
    userInfo[0] = userX
    userInfo[1] = userY
    return userInfo
    
#Check to see if anyone won
#To check win, we need to check board[x][0-2], board[0-2][y], if x == y check top to bottom diagnol, and if (x == 2 and y == 0) or (x == 0 and y == 2) check bottom to top diagnal. (if x == y == 1, check both diagnols)
def checkWin(info):
    xCount=0
    oCount=0
    
    #for loop through board[0-2][y]
    for x in randomNumberList:
        if board[info[0]][x] == 'X':
            xCount+=1
        elif board[info[0]][x] == 'O':
            oCount+=1
        if xCount == 3:
            return 'X'
        elif oCount == 3:
            return 'O'
            
    xCount=0
    oCount=0
    #for loop through board[x][0-2]
    for x in randomNumberList:
        if board[x][info[1]] == 'X':
            xCount+=1
        elif board[x][info[1]] == 'O':
            oCount+=1
        if xCount == 3:
            return 'X'
        elif oCount == 3:
            return 'O'
    
    #checks to see if we need to check diagnals
    #both diagnals need to be checked
    #if info[0] == info[1] and info[0] == 1:
       #I dont think this is needed
    #top left to bottom right diagnal needs to be checked
    if info[0] == info[1]:
        if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
            return 'X'
        elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
            return 'O'
    #bottom left to top right diagnal needs to be checked
    if (info[0] == 2 and info[1] == 0) or (info[0] == 0 and info[1] == 2) or (info[0] == 1 and info[1] == 1):
        if board[0][2] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
            return 'X'
        elif board[0][2] == 'O' and board[1][1] == 'O' and board[0][2] == 'O':
            return 'O'
    for x in randomNumberList:
        for c in randomNumberList:
            if ' ' in board[x][c]:
                return 'Y'
    return 'Z'
    
    
#choses the location of the computers move
#need to make this guy smarter
def computersMove():
    chosing = True
    print("Computer's Move:")
    while(chosing):
        computerX = random.choice(randomNumberList)
        computerY = random.choice(randomNumberList)
        
        if board[computerX][computerY] == ' ':
            board[computerX][computerY] = 'O'
            chosing = False
    computerInfo = [0] * 2
    computerInfo[0] = computerX
    computerInfo[1] = computerY
    return computerInfo
    
#print board
def printBoard():
    for x in randomNumberList:
        for c in randomNumberList:
            if c == 2:
                print(board[x][c],end = " ")
            else:
                print(board[x][c],end = "|")
        if x == 0 or x == 1:
            print()
            print("-----")
        else:
            print()
    print()

#main function
def main():
    turn = True
    #Users info - turn, x, y
    userInfo = [0] * 3
    continueGame = True
    winCheck = 'A'
    
    #Computer info - turn, x, y
    computerInfo = [0] * 3
    while continueGame:
        printBoard()
        if turn:
            userInfo = enterMove()
            turn = False
            winCheck = checkWin(userInfo)
            continueGame = winCheck == 'Y'
        else:
            computerInfo = computersMove()
            turn = True
            winCheck = checkWin(computerInfo)
            continueGame = winCheck == 'Y'
        
        
    if winCheck == 'X':
        print("You win!")
    elif winCheck == 'O':
        print("You lose!")
    elif winCheck == 'Z':
        print("Tie Game!")
    else:
        print("Something fucked up")
    
    
main()