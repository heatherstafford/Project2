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
    board = [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]

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
    print(ship1col, ship2col, ship3col)
    
def computerTurn(): 
    return
def mouseClick(event):
    if event.x <= 50:
        col = 1
    elif event.x <= 100:
        col = 2
    elif event.x <= 150:
        col = 3
    elif event.x <= 200:
        col = 4
    elif event.x <= 250:
        col = 5
    else:
        print('Invalid Space')
        
    if event.y <= 50:
        row = 1
    elif event.y <= 100:
        row = 2
    elif event.y <= 150:
        row = 3
    elif event.y <= 200:
        row = 4
    elif event.y <= 250:
        row = 5
    else:
        print('Invalid Space')
        
 
    
if __name__ == '__main__': 
    
    data = {}
    
    boardgraphics = RectangleAsset(RADIUS,RADIUS,LineStyle(1,black),white)
    ships = RectangleAsset(RADIUS,RADIUS,LineStyle(1,black),blue)

    redrawAll()
    pickComputerShips()
    
    App().listenMouseEvent('click', mouseClick)
    App().run()
    