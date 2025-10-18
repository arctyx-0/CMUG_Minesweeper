from cmu_graphics import *
import random

# app variables
app.height = 500
app.background = "gray"

squares = []
topSquares = []
mines = []
numbers = []

def generateBoard():
    num = 0
    y = 100
    for i in range(10):
        x = 0
        for j in range(10):
            gold = Rect(x, y, 40, 40, fill='gold', border='gray')
            gray = Rect(x, y, 40, 40, fill='darkGray', border='gray')
            squares.append(gold)
            topSquares.append(gray)
            x += 40
            num += 1
        y += 40

def generateMines():
  for i in range(100):
    mines.append(False)
    numbers.append(0)
  placed = 0
  while placed < 15:
      r = random.randint(0,99)
      if not mines[r]:
          mines[r] = True
          placed += 1
  for i in range(100):
      if mines[i]:
          continue
      count = 0
      for j in [-1, 1, -10, 10, -11, -9, 9, 11]: #checks the fucking surrounding squares
          check = i + j
          if 0 <= check < 100 and mines[check]:#checks to see if squares exist
            if abs((check % 10) - (i % 10)) <= 1:#prevents wrapping for detection
                count += 1
      numbers[i] = count

def onMousePress(x, y):
    for i in range(100):
        if topSquares[i].contains(x, y):
            topSquares[i].visible = False
            if mines[i]:
                Label('boom', squares[i].centerX, squares[i].centerY, size=20)
            elif numbers[i] > 0:
                Label(str(numbers[i]), squares[i].centerX, squares[i].centerY, size=20)
            break


generateBoard()
generateMines()
cmu_graphics.run() # type: ignore
