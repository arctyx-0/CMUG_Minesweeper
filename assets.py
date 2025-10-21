from dataclasses import dataclass
from random import randint

from cmu_graphics import Group, Circle, Line

@dataclass
class Assets:
    def drawMine() -> Group:
        mineBody = Circle(
          200,200,
          100
        )
        mineSpoke_NS = Line(
            200,50,
            200,350,
            lineWidth=20
        )
        mineSpoke_EW = Line(
            50,200,
            350,200,
            lineWidth=20
        )
        mineSpoke_NWSE = Line(
            100,100,
            300,300,
            lineWidth=20
        )
        mineSpoke_NESW = Line(
            300,100,
            100,300,
            lineWidth=20
        )
        reflection = Circle(
            random.randint(mineBody.centerX-50,mineBody.centerX+50),
            random.randint(mineBody.centerY-50,mineBody.centerY+50),
            30,
            fill="white"
        )
        
        mineSprite = Group( mineBody, mineSpoke_NS, mineSpoke_EW, mineSpoke_NWSE, mineSpoke_NESW, reflection )
        return mineSprite
    
    def drawFlag():
        raise NotImplementedError("Sprite in development")
        
        '''flagSpirte = Group(  )
        return flagSpirte'''
