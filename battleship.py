#Heather Stafford
#5/23/18
#battleship.py - project2

from ggame import *

white = Color(0xFFFFFF)
black = Color(0x000000)

def buildBoard():
    board = [['','',''],['','',''],['','',''],['','',''],['','','']]

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for r in range(0,5):
        for c in range(0,5):
            boardgraphics = RectangleAsset(10,10,LineStyle(1,black),white)
            Sprite(boardgraphics)

if __name__ == '__main__': 
    
    redrawAll()
    
    App().run()
    