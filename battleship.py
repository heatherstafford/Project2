#Heather Stafford
#5/23/18
#battleship.py - project2

from ggame import *
from random import randint

RADIUS = 50

white = Color(0xFFFFFF,1)
black = Color(0x000000,1)

def buildBoard():
    board = [['','',''],['','',''],['','',''],['','',''],['','','']]

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for r in range(5):
        for c in range(5):
            Sprite(boardgraphics,((RADIUS)*r,(RADIUS)*c))
            Sprite(boardgraphics,(((RADIUS)*r) + 400,(RADIUS)*c))

def pickComputerShips():
    ship1row = randint(0,5)
    ship2row = randint(0,5)
    while ship2row == ship1row:
        ship2row = randint(0,5)
    ship3row = randint(0,5)
    while ship3row == ship1row or ship3row == ship2row:
        ship3row = randint(0,5)
    print(ship1row, ship2row, ship3row)
    
    ship1col = randint(0,5)
    ship2col = randint(0,5)
    ship3col = randint(0,5)
    
    """
    while ship2col == ship1row:
        ship2col = randint(0,5)
    ship3col = randint(0,5)
    while ship3col == ship1col or ship3col == ship2col:
        ship3col = randint(0,5)
    """
    print(ship1col, ship2col, ship3col)
    
if __name__ == '__main__': 
    
    boardgraphics = RectangleAsset(RADIUS,RADIUS,LineStyle(1,black),white)

    redrawAll()
    pickComputerShips()
    
    App().run()
    