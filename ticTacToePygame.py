# Copyright: Thomas Oakes 2021
# Tic Tac Toe using pygame
import pygame
from array import *
import random
from pygame import mixer

#initialize pygame
pygame.init()

#creates the screen
screen = pygame.display.set_mode((800,600))

#titel and icon change
pygame.display.set_caption("Tic Tac Toe")
#go to flaticon.com or and look for an icon or make an icon to import into the project
icon = pygame.image.load('board.png')
pygame.display.set_icon(icon)

#background image
background = pygame.image.load('background.jpg')

# Background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# stores the width of the
# screen into a variable
width = screen.get_width()
  
# stores the height of the
# screen into a variable
height = screen.get_height()

page = '1'

board = [
         [' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']
         ]

randomNumberList = [0,1,2]
gameMode = 0
global turn
turn = 1

#quadrant 1
qOneXStart = 200
qOneYStart = 75
#quadrant 2
qTwoXStart = 350
qTwoYStart = 75
#quadrant 3
qThreeXStart = 500
qThreeYStart = 75
#quadrant 4
qFourXStart = 200
qFourYStart = 225
#quadrant 5
qFiveXStart = 350
qFiveYStart = 225
#quadrant 6
qSixXStart = 500
qSixYStart = 225
#quadrant 7
qSevenXStart = 200
qSevenYStart = 375
#quadrant 8
qEightXStart = 350
qEightYStart = 375
#quadrant 9
qNineXStart = 500
qNineYStart = 375

dispFont = pygame.font.Font('freesansbold.ttf', 96)

#displays the first screen
#Page one - title screen that allows user to select one or two player mode
def displayPage1():
    #displays title
    titleFont = pygame.font.Font('freesansbold.ttf', 96)
    title = titleFont.render("Tic Tac Toe",True,(0,0,0))    
    screen.blit(title, (154, 50))
    
    #draws buttons
    pygame.draw.rect(screen,(170,170,170),[330,300,140,40])
    pygame.draw.rect(screen,(170,170,170),[330,375,140,40])
    
    #displays options
    playerFont = pygame.font.Font('freesansbold.ttf', 16)
    onePlayer = playerFont.render("One Player",True,(0,0,0))    
    screen.blit(onePlayer, (360, 312))          #width is button width+30 and height is button height+12
    
    twoPlayer = playerFont.render("Two Player",True,(0,0,0))    
    screen.blit(twoPlayer, (360, 387))          #width is button width+30 and height is button height+12

#displays the second page
#Page two - board screen
def displayPage2():
    #displays title
    titleFont2 = pygame.font.Font('freesansbold.ttf', 36)
    title2 = titleFont2.render("Tic Tac Toe",True,(0,0,0))    
    screen.blit(title2, (20, 20))
    
    #draws board
    pygame.draw.rect(screen,(0,0,0),[330,75,20,450])
    pygame.draw.rect(screen,(0,0,0),[480,75,20,450])
    pygame.draw.rect(screen,(0,0,0),[190,205,450,20])
    pygame.draw.rect(screen,(0,0,0),[190,355,450,20])
    
    #debugging click areas
    #pygame.draw.rect(screen,(60,60,60),[qOneXStart,qOneYStart,130,130])
    #pygame.draw.rect(screen,(60,60,60),[qTwoXStart,qTwoYStart,130,130])
    #pygame.draw.rect(screen,(60,60,60),[qThreeXStart,qThreeYStart,130,130])
    #pygame.draw.rect(screen,(60,60,60),[qFourXStart,qFourYStart,130,130])
    #pygame.draw.rect(screen,(60,60,60),[qFiveXStart,qFiveYStart,130,130])
    #pygame.draw.rect(screen,(60,60,60),[qSixXStart,qSixYStart,130,130])
    #pygame.draw.rect(screen,(60,60,60),[qSevenXStart,qSevenYStart,130,130])
    #pygame.draw.rect(screen,(60,60,60),[qEightXStart,qEightYStart,130,130])
    #pygame.draw.rect(screen,(60,60,60),[qNineXStart,qNineYStart,130,130])
    
    
def checkMove(x, letter):
    a = 0
    b = 0
    
    if x == 1:
        a = 0
        b = 0
    elif x == 2:
        a = 0
        b = 1
    elif x == 3:
        a = 0
        b = 2
    elif x == 4:
        a = 1
        b = 0
    elif x == 5:
        a = 1
        b = 1
    elif x == 6:
        a = 1
        b = 2
    elif x == 7:
        a = 2
        b = 0
    elif x == 8:
        a = 2
        b = 1
    elif x == 9:
        a = 2
        b = 2
    else:
        return False
    if board [a][b] == ' ':
        board[a][b] = letter
        return True
    return False

#choses the location of the computers move
#need to make this guy smarter
def computersMove():
    chosing = True
    #print("Computer's Move:")
    while(chosing):
        computerX = random.choice(randomNumberList)
        computerY = random.choice(randomNumberList)
        
        if board[computerX][computerY] == ' ':
            board[computerX][computerY] = 'O'
            chosing = False
    
def addMove(x, move):
    localTurn = move
    if gameMode == 1:
        #Player 1 turn
        if localTurn%2 != 0:
            if checkMove(x, 'X'):
                #turn increment 
                localTurn +=1
                printBoard()
                if checkWin(x) != 1:
                    computersMove()
                    localTurn +=1
    elif gameMode == 2:
        #Player 1 turn
        if localTurn%2 != 0:
            if checkMove(x, 'X'):
                #turn increment 
                localTurn +=1
        #Player 2 turn
        elif localTurn%2 == 0:
            if checkMove(x, 'O'):
                #turn increment 
                localTurn +=1
    return localTurn

def printBoard():
    for x in randomNumberList:
        for c in randomNumberList:
            #if board[x][c] != ' ':
            letterX = 220 + (150*c)
            letterY = 105 + (150*x)
            
            dispLetter = dispFont.render(board[x][c],True,(0,0,0))    
            screen.blit(dispLetter, (letterX, letterY))
    
def checkWin(x):
    xCount=0
    oCount=0
    a = 0
    b = 0
    
    if x == 1:
        a = 0
        b = 0
    elif x == 2:
        a = 0
        b = 1
    elif x == 3:
        a = 0
        b = 2
    elif x == 4:
        a = 1
        b = 0
    elif x == 5:
        a = 1
        b = 1
    elif x == 6:
        a = 1
        b = 2
    elif x == 7:
        a = 2
        b = 0
    elif x == 8:
        a = 2
        b = 1
    elif x == 9:
        a = 2
        b = 2
    
    #for loop through board[0-2][y]
    for z in randomNumberList:
        if board[a][z] == 'X':
            xCount+=1
        elif board[a][z] == 'O':
            oCount+=1
        if xCount == 3:
            return 1
        elif oCount == 3:
            return 2
            
    xCount=0
    oCount=0
    #for loop through board[x][0-2]
    for z in randomNumberList:
        if board[z][b] == 'X':
            xCount+=1
        elif board[z][b] == 'O':
            oCount+=1
        if xCount == 3:
            return 1
        elif oCount == 3:
            return 2
    
    #checks to see if we need to check diagnals
    #both diagnals need to be checked
    #if info[0] == info[1] and info[0] == 1:
    #top left to bottom right diagnal needs to be checked
    if a == b:
        if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
            return 1
        elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
            return 2
    #bottom left to top right diagnal needs to be checked
    if (a == 2 and b == 0) or (a == 0 and b == 2) or (a == 1 and b == 1):
        if board[0][2] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
            return 1
        elif board[0][2] == 'O' and board[1][1] == 'O' and board[0][2] == 'O':
            return 2
    for x in randomNumberList:
        for c in randomNumberList:
            if ' ' in board[x][c]:
                return 0
    return 3
    
def displayGameOverText(x):
    #draws board
    pygame.draw.rect(screen,(0,0,0),[330,75,20,450])
    pygame.draw.rect(screen,(0,0,0),[480,75,20,450])
    pygame.draw.rect(screen,(0,0,0),[190,205,450,20])
    pygame.draw.rect(screen,(0,0,0),[190,355,450,20])
    
    #displays Game Over
    gameOverFont = pygame.font.Font('freesansbold.ttf', 96)
    gameOver = gameOverFont.render("GAME OVER",True,(255,0,0))
    screen.blit(gameOver, (120, 200))
    
    resultFont = pygame.font.Font('freesansbold.ttf', 48)
    
    if x == 1:
        resultText = resultFont.render("Player 1 Wins!",True,(29,168,52))
    elif x == 2:
        if gameMode == 1:
            resultText = resultFont.render("Computer Wins!",True,(29,168,52))
        elif gameMode == 2:
            resultText = resultFont.render("Player 2 Wins!",True,(29,168,52))
    elif x == 3:
        resultText = resultFont.render("Tie Game!",True,(29,168,52))
    else:
        resultText = resultFont.render("Something Fucked up!",True,(29,168,52))
    screen.blit(resultText, (250, 10))
        
    # Main menu button
    menuFont = pygame.font.Font('freesansbold.ttf', 16)
    pygame.draw.rect(screen,(170,170,170),[330,375,200,75])    
    menu = menuFont.render("Main Menu",True,(0,0,0))    
    screen.blit(menu, (380, 395))          #width is button width+30 and height is button height+12

# Resets game
def newGame(count):
    page = '1'
    board[0][0] = ' '
    board[0][1] = ' '
    board[0][2] = ' '
    board[1][0] = ' '
    board[1][1] = ' '
    board[1][2] = ' '
    board[2][0] = ' '
    board[2][1] = ' '
    board[2][2] = ' '
    gameMode = 0
    turn = 1
    screenWait = False
    screenWait2 = False
    displayLetters = True
    win = 0
    menuFont = pygame.font.Font('freesansbold.ttf', 16)   
    menu = menuFont.render(str(count),True,(0,0,0))    
    screen.blit(menu, (10, 10))          #width is button width+30 and height is button height+12

# Game loop
count=0;
running = True
turn = 1
quad = 0
screenWait = False
screenWait2 = False
screenWait3 = True
displayLetters = True
#0 = nothing
#1 = first player wins
#2 = computer or player two wins
#3 = tie
win = 0
while running:
    # Background image
    screen.blit(background, (0,0))
    if page == '1':
        count = 1 
        displayPage1()
        screenWait3 = True
    elif page == '2':
        count = 2 
        displayPage2()
        screenWait3 = False
        screenWait = True
    elif page == '3':
        count = 3 
        displayLetters = False
        printBoard()
        displayGameOverText(win)
        screenWait2 = True

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        # Page one
        if page == '1' and screenWait3:
            #checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if the mouse is clicked on the
                # Clicling One Player
                if 330 <= mouse[0] <=470 and 300 <= mouse[1] <= 340:
                    gameMode = 1
                    page = '2'
                # Clicling Two Player
                if 330 <= mouse[0] <= 470 and 375 <= mouse[1] <= 415:
                    gameMode = 2
                    page = '2'
                #TODO: add options button 
        # Page two
        if page == '2' and screenWait:
            #checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                #first quadrant
                if qOneXStart <= mouse[0] <= qOneXStart+130 and qOneYStart <= mouse[1] <=qOneYStart+130:
                    quad = 1
                #2nd quadrant
                elif qTwoXStart <= mouse[0] <= qTwoXStart+130 and qTwoYStart <= mouse[1] <=qTwoYStart+130:
                    quad = 2
                #3rd quadrant
                elif qThreeXStart <= mouse[0] <= qThreeXStart+130 and qThreeYStart <= mouse[1] <=qThreeYStart+130:
                    quad = 3
                #4th quadrant
                elif qFourXStart <= mouse[0] <= qFourXStart+130 and qFourYStart <= mouse[1] <=qFourYStart+130:
                    quad = 4
                #5th quadrant
                elif qFiveXStart <= mouse[0] <= qFiveXStart+130 and qFiveYStart <= mouse[1] <=qFiveYStart+130:
                    quad = 5
                #6th quadrant
                elif qSixXStart <= mouse[0] <= qSixXStart+130 and qSixYStart <= mouse[1] <=qSixYStart+130:
                    quad = 6
                #7th quadrant
                elif qSevenXStart <= mouse[0] <= qSevenXStart+130 and qSevenYStart <= mouse[1] <=qSevenYStart+130:
                    quad = 7
                #8th quadrant
                elif qEightXStart <= mouse[0] <= qEightXStart+130 and qEightYStart <= mouse[1] <=qEightYStart+130:
                    quad = 8
                #9th quadrant
                elif qNineXStart <= mouse[0] <= qNineXStart+130 and qNineYStart <= mouse[1] <=qNineYStart+130:
                    quad = 9
                turn = addMove(quad, turn)
                #Check if gameOver
                win = checkWin(quad)
                if win != 0:
                    page = '3'
                # Page two
        if page == '3' and screenWait2:
            #checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Checks if main menu button is clicked
                if 300 <= mouse[0] <= 500 and 375 <= mouse[1] <= 450:
                    newGame(count)
                    page = '1'
                    board[0][0] = ' '
                    board[0][1] = ' '
                    board[0][2] = ' '
                    board[1][0] = ' '
                    board[1][1] = ' '
                    board[1][2] = ' '
                    board[2][0] = ' '
                    board[2][1] = ' '
                    board[2][2] = ' '
 
    #main()
    if displayLetters:
        printBoard()
    pygame.display.update()    