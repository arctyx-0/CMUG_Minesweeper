from cmu_graphics import *
from utils import Utils, Colors

import time
import random
import sys
import os

os.system("clear")

sys.setrecursionlimit(1000)

# app variables
app.height = 500
app.background = "gray"


cols = 10
rows = 10
total = cols * rows
squares = []
topSquares = []
mines = []
numbers = []


restartLabel: str = ":3"
def drawTopBar():
    def magicLengthReducer1(x):
        # reduces file length. !! USE WITH THE UNPACKING OPERATOR !!
        returnList = [
            x,15,
            100,60
        ]
        return returnList

    background = Rect(
        0,0,
        400,95,
        fill=Colors.gray
    )
    borderBottom = Rect(
        0,90,
        400,10,
        fill=Colors.darkGray
    )

    restartButton = Rect(
        175,15,
        50,60,
        fill=Colors.darkGray
    )
    restartButtonLabel = Label(
        restartLabel,
        restartButton.centerX,restartButton.centerY,
        font="arial",
        fill=Colors.red,
        size=35
    )
    restartButtonLabel.rotate(90, restartButton.centerX, restartButton.centerY)
    global restart; restart = Group( restartButton, restartButtonLabel )

    clockBackground = Rect( *magicLengthReducer1(50), fill=Colors.darkGray )
    # NOTE: the clocks label is drawn in a separate function

    flagBackground = Rect( *magicLengthReducer1(250), fill=Colors.darkGray )
    # NOTE: the flag count is drawn in a separate function

def generateBoard():
    num = 0
    y = 100
    for i in range(rows):
        x = 0
        for j in range(cols):
            gold = Rect(x, y, 40, 40, fill='gold', border='gray')
            gray = Rect(x, y, 40, 40, fill='darkGray', border='gray')
            squares.append(gold)
            topSquares.append(gray)
            x += 40
            num += 1
        y += 40

def generateMines():
  for i in range(total):
    mines.append(False)
    numbers.append(0)
  placed = 0
  while placed < 15:
      r = random.randint(0, total - 1)
      if not mines[r]:
          mines[r] = True
          placed += 1
  for i in range(total):
      if mines[i]:
          continue
      count = 0
      for j in [-1, 1, -cols, cols, -cols-1, -cols+1, cols-1, cols+1]: #checks the fucking surrounding squares
          check = i + j
          if 0 <= check < total and mines[check]:#checks to see if squares exist
            if abs((check % cols) - (i % cols)) <= 1:#prevents wrapping for detection
                count += 1
      numbers[i] = count

def onMousePress(x, y):
    for i in range(total):
        if topSquares[i].contains(x, y):
            topSquares[i].visible = False
            if mines[i]:
                Label('boom', squares[i].centerX, squares[i].centerY, size=20, fill=Colors.red)
            elif numbers[i] > 0:
                numberLabel = Label(str(numbers[i]), squares[i].centerX, squares[i].centerY, size=20)
                if numberLabel.value == "1": numberLabel.fill = Colors.number.one
                elif numberLabel.value == "2": numberLabel.fill = Colors.number.two
                elif numberLabel.value == "3": numberLabel.fill = Colors.number.three
                elif numberLabel.value == "4": numberLabel.fill = Colors.number.four
                elif numberLabel.value == "5": numberLabel.fill = Colors.number.five
                elif numberLabel.value == "6": numberLabel.fill = Colors.number.six
                elif numberLabel.value == "7": numberLabel.fill = Colors.number.seven
                elif numberLabel.value == "8": numberLabel.fill = Colors.number.eight
                else: numberLabel.fill = None
            else: #clearing an area (no 0 squares next to a unrevealed square)
                for j in [-1, 1, -cols, cols, -cols-1, -cols+1, cols-1, cols+1]: #checks the fucking surrounding squares
                    adjTile = i + j
                    print(adjTile)
                    if adjTile>(len(topSquares)-1) or adjTile<0: continue
                    if not mines[adjTile] and abs((adjTile % cols) - (i % cols)) <= 1 and topSquares[adjTile].visible == True:
                        onMousePress(topSquares[adjTile].centerX,topSquares[adjTile].centerY)
            break

    # restarts the game
    ## TODO: figure out why it only closes the
    ## program and not restarts it
    # if restart.hits(x, y): Utils.restart()

def onKeyRelease(key):
    # restarts the game
    if key == 'r': Utils.restart()
    # closes the game
    if key == 'x': exit()


generateBoard()
generateMines()
drawTopBar()

cmu_graphics.run() # type: ignore
