#Heather Stafford
#5/23/18
#battleship.py - project2

from ggame import *

def buildBoard():
    for r in range(0,3):
        for c in range(0,3):
            print(board[r][c], end=' ')
        print()

board = [['','',''],['','',''],['','','']]
            
def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()

if __name__ == '__main__': 
    
    App().run()
    