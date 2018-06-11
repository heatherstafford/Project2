#Heather Stafford
#5/23/18
#battleship.py - project2

from ggame import *
from random import randint

#size of the boxes
RADIUS = 50

#colors
white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
blue = Color(0x0000FF,1)
red = Color(0xFF0000,1)

#creates and returns a 5x5 empty matrix
def buildBoard():
    return[['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]

#deletes all the graphics on the board and redraws the player board and computer board in their current state
def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for r in range(5):
        for c in range(5):
            Sprite(boardgraphics,((RADIUS)*c,(RADIUS)*r))
            if data['matrix'][r][c] == 'ship':
                Sprite(ships,((RADIUS)*c,(RADIUS)*r))
            elif data['matrix'][r][c] == 'hit':
                Sprite(hit,(((RADIUS)*c),(RADIUS)*r))
            elif data['matrix'][r][c] == 'miss':
                Sprite(miss,(((RADIUS)*c),(RADIUS)*r))
            Sprite(boardgraphics,(((RADIUS)*c) + 400,(RADIUS)*r))
            Sprite(computerboard, (430, 250))
            Sprite(playerboard, (70,250))
            if data['boatmatrix'][r][c] == 'hit':
                Sprite(hit,(((RADIUS)*c) + 400,(RADIUS)*r))
            elif data['boatmatrix'][r][c] == 'miss':
                Sprite(miss,(((RADIUS)*c) + 400,(RADIUS)*r))
            if data['playershipsSunk'] == 3:
                Sprite(playerwinner, (280,200))
            if data['boatshipsSunk'] == 3:
                Sprite(computerwinner, (270, 200))
            
#the computer chooses three random places to put ships, and not on top of each other
def pickComputerShips():
    ship1row = randint(0,4)
    ship2row = randint(0,4)
    while ship2row == ship1row:
        ship2row = randint(0,4)
    ship3row = randint(0,4)
    while ship3row == ship1row or ship3row == ship2row:
        ship3row = randint(0,4)
    
    ship1col = randint(0,4)
    ship2col = randint(0,4)
    ship3col = randint(0,4)
    
    data['boatmatrix'][ship1row][ship1col] = 'ship'
    data['boatmatrix'][ship2row][ship2col] = 'ship'
    data['boatmatrix'][ship3row][ship3col] = 'ship'

#The computer chooses a random row and column to guess for a ship on the players board
#updates the matrix that holds information about hit, miss, or ship
def computerTurn(): 
    guessrow = randint(0,4)
    guesscol = randint(0,4)
    if data['matrix'][guessrow][guesscol] != 'hit' and data['matrix'][guessrow][guesscol] != 'miss':
        if data['matrix'][guessrow][guesscol] == 'ship':
            data['matrix'][guessrow][guesscol] = 'hit'
            data['boatshipsSunk'] += 1
        else:
            data['matrix'][guessrow][guesscol] = 'miss'
    else: 
        computerTurn()
    redrawAll()

#figures out what column and row the player clicked for a ship
#once the player places three ships the player guesses for computer ships
#it updates the matrix that holds information about hit, miss, or ship
def mouseClick(event):
    row = event.y // 50
    col = event.x // 50
    
    if data['shipnumber'] < 3:
        data['matrix'][row][col] = 'ship'
        data['shipnumber'] += 1
    else:
        col = (event.x - 400) // 50
        if data['boatmatrix'][row][col] == 'ship':
            data['boatmatrix'][row][col] = 'hit'
            data['playershipsSunk'] += 1
        else:
            data['boatmatrix'][row][col] = 'miss'
        computerTurn()
    redrawAll()
    
#sets up the game
if __name__ == '__main__': 
    
    #dictionary
    data = {}
    data['matrix'] = buildBoard()
    data['boatmatrix'] = buildBoard()
    data['shipnumber'] = 0
    data['boatnumber'] = 0
    data['boatshipsSunk'] = 0
    data['playershipsSunk'] = 0
    
    #all the graphics used
    boardgraphics = RectangleAsset(RADIUS,RADIUS,LineStyle(1,black),white)
    ships = RectangleAsset(RADIUS,RADIUS,LineStyle(1,black),blue)
    hit = RectangleAsset(RADIUS,RADIUS,LineStyle(1,black),red)
    miss = CircleAsset(RADIUS/2,LineStyle(1,black),white)
    computerwinner = TextAsset('The Computer Wins!', fill = black, style = 'italic 35pt times')
    playerwinner = TextAsset('The Player Wins!', fill = black, style = 'italic 35pt times')
    playerboard = TextAsset('Player Board', fill = black, style = 'italic 35pt times')
    computerboard = TextAsset('Computer Board', fill = black, style = 'italic 35pt times')

    redrawAll()
    pickComputerShips()
    App().listenMouseEvent('click', mouseClick)
    App().run()
    