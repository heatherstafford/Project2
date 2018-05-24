#Heather Stafford
#5/23/18
#battleship.py - project2

from ggame import *

white = Color(0xFFFFFF,1)
black = Color(0x000000,1)

def buildBoard():
    board = [['','',''],['','',''],['','',''],['','',''],['','','']]

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
        boardgraphics = RectangleAsset(30,30,LineStyle(1,black),white)

if __name__ == '__main__': 
    
    redrawAll()
    for r in range(5):
        for c in range(5):
            Sprite(RectangleAsset(30,30,LineStyle(1,black),white))
    
    App().run()
    