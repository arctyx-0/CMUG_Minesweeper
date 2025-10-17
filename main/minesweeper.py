from cmu_graphics import *

# app variables
app.height = 500
app.background = "gray"

squareNum = 0
squareNumText = f"topSquare{squareNum}"
bSquareNumText = f"bSquare{squareNum}"

def generateBoard():
    global squareNumText, squareNum
    for i in range(10):
      ymodifier = i*40
      for j in range(10):
          xmodifier = j*40
          globals()[bSquareNumText] = Rect(0+xmodifier,100+ymodifier,40,40,fill="gold",border="gray",borderWidth=1)
          globals()[squareNumText] = Rect(0+xmodifier,100+ymodifier,40,40,fill="darkGray",border="gray",borderWidth=1)
          squareNum += 1
          squareNumText = f"topSquare{squareNum}"
          bSquareNumText = f"bSquare{squareNum}"

def onMousePress(x, y):
   print(x, y)

generateBoard()

cmu_graphics.run() # type: ignore
