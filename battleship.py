#Heather Stafford
#5/23/18
#battleship.py - project2

from ggame import *

RADIUS = 30

white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
boardgraphics = RectangleAsset(RADIUS,RADIUS,LineStyle(1,black),white)

def buildBoard():
    board = [['','',''],['','',''],['','',''],['','',''],['','','']]

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for r in range(25):
        for c in range(25):
            Sprite(boardgraphics(10 + (2*RADIUS+10)*r,10 + (2*RADIUS+10)*c))

if __name__ == '__main__': 
    

    redrawAll()
    
    App().run()
    