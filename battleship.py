#Heather Stafford
#5/23/18
#battleship.py - project2

from ggame import *

def buildBoard():
    board = [['','',''],['','',''],['','','']]

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    for r in range(0,5):
        for c in range(0,5):

if __name__ == '__main__': 
    
    App().run()
    