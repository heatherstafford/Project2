#Heather Stafford
#5/23/18
#battleship.py - project2

from ggame import *
from random import randint

RADIUS = 50

white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
blue = Color(0x0000FF,1)
red = Color(0xFF0000,1)

def buildBoard():
    return[['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]

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
            if data['boatmatrix'][r][c] == 'ship':
                Sprite(ships,(((RADIUS)*c) + 400,(RADIUS)*r))
            elif data['boatmatrix'][r][c] == 'hit':
                Sprite(hit,(((RADIUS)*c) + 400,(RADIUS)*r))
            elif data['boatmatrix'][r][c] == 'miss':
                Sprite(miss,(((RADIUS)*c) + 400,(RADIUS)*r))

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
        
    if data['shipsSunk'] == 3:
        Sprite(computerwinner, (200, 200))
    
    redrawAll()

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
    
if __name__ == '__main__': 
    
    data = {}
    data['matrix'] = buildBoard()
    data['boatmatrix'] = buildBoard()
    data['shipnumber'] = 0
    data['boatnumber'] = 0
    data['boatshipsSunk'] = 0
    data['playershipsSunk'] = 0
    
    boardgraphics = RectangleAsset(RADIUS,RADIUS,LineStyle(1,black),white)
    ships = RectangleAsset(RADIUS,RADIUS,LineStyle(1,black),blue)
    hit = RectangleAsset(RADIUS,RADIUS,LineStyle(1,black),red)
    miss = CircleAsset(RADIUS/2,LineStyle(1,black),white)
    computerwinner = TextAsset('The Computer Wins!', fill = black, style = 'italic 35pt times')
    playerwinner = TextAsset('The Player Wins!', fill = black, style = 'italic 35pt times')

    redrawAll()
    pickComputerShips()
    
    App().listenMouseEvent('click', mouseClick)
  
    App().run()
    