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
    ship1 = randint(0,5)
    ship2 = randint(0,5)
    if ship2 == ship1:
        ship2 = randint(0,5)
    ship3 = randint(0,5)
    if ship3 == ship1 or ship3 == shi2:
        ship3 = randint(0,5)
    print(ship1, ship2, ship3, ship4)
    
if __name__ == '__main__': 
    
    boardgraphics = RectangleAsset(RADIUS,RADIUS,LineStyle(1,black),white)

    redrawAll()
    
    App().run()
    