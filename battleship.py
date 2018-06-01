#Heather Stafford
#5/23/18
#battleship.py - project2

from ggame import *
from random import randint

RADIUS = 50

white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
blue = Color(0xFF0000,1)

def buildBoard():
    return[['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for r in range(5):
        for c in range(5):
            Sprite(boardgraphics,((RADIUS)*r,(RADIUS)*c))
            Sprite(boardgraphics,(((RADIUS)*r) + 400,(RADIUS)*c))
    print(data['matrix'])
            

def pickComputerShips():
    ship1row = randint(-1,4)
    ship2row = randint(-1,4)
    while ship2row == ship1row:
        ship2row = randint(-1,4)
    ship3row = randint(-1,4)
    while ship3row == ship1row or ship3row == ship2row:
        ship3row = randint(-1,4)
    
    ship1col = randint(-1,4)
    ship2col = randint(-1,4)
    ship3col = randint(-1,4)
    
    data['boatmatrix'][ship1row][ship1col] = 'ship'
    data['boatmatrix'][ship2row][ship2col] = 'ship'
    data['boatmatrix'][ship3row][ship3col] = 'ship'
    
    print(data['boatmatrix'])
    
def computerTurn(): 
    guessrow = randint(-1,4)
    guesscol = randint(-1,4)
    data['guessmatrix'][guessrow][guesscol] = 'ship'
    if data['guessmatrix'] == data['matrix']:
        print(good)

def mouseClick(event):
    row = event.y // 50
    col = event.x // 50
        
    data['matrix'][row][col] = 'ship'
    redrawAll()

    
if __name__ == '__main__': 
    
    data = {}
    data['matrix'] = buildBoard()
    data['boatmatrix'] = buildBoard()
    data['guessmatrix'] = buildBoard()

    
    boardgraphics = RectangleAsset(RADIUS,RADIUS,LineStyle(1,black),white)
    ships = RectangleAsset(RADIUS,RADIUS,LineStyle(1,black),blue)

    redrawAll()
    pickComputerShips()
    
    App().listenMouseEvent('click', mouseClick)
    App().run()
    