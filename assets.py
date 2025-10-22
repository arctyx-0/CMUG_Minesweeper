from dataclasses import dataclass
from random import randint

from cmu_graphics import Group, Circle, Line, Polygon

@dataclass
class Assets:
    @staticmethod
    def mine(x: int, y: int, scale: float = 1.0, 
             doSetRotation: bool = False, setRotation: int = 0, doRandomRotation: bool = False) -> Group:
    
        mineBody = Circle(
            x,y,
            100*scale
        )
        mineSpoke_NS = Line(
            x,y-(150*scale),
            x,y+(150*scale),
            lineWidth=20*(scale*1.4)
        )
        mineSpoke_EW = Line(
            x-150*scale,y,
            x+150*scale,y,
            lineWidth=20*(scale*1.4)
        )
        mineSpoke_NWSE = Line(
            x-100*scale,y-100*scale,
            x+100*scale,y+100*scale,
            lineWidth=20*(scale*1.4)
        )
        mineSpoke_NESW = Line(
            x+100*scale,y-100*scale,
            x-100*scale,y+100*scale,
            lineWidth=20*(scale*1.4)
        )
        reflection = Circle(
            randint(int(x-50*scale),int(x+50*scale)),
            randint(int(y-50*scale),int(y+50*scale)),
            30*(scale*0.9),
            fill="white"
        )
        
        mineSprite = Group( mineBody, mineSpoke_NS, mineSpoke_EW, mineSpoke_NWSE, mineSpoke_NESW, reflection )

        # default rotation, do not change 
        mineSprite.rotate(45, mineBody.centerX, mineBody.centerY)
        
        if doSetRotation == True:
            mineSprite.rotate(setRotation, mineBody.centerX, mineBody.centerY)
        else:
            pass
        
        if doRandomRotation == True:
            mineSprite.rotate(randint(0,359), mineBody.centerX, mineBody.centerY)
        else: 
            pass
        
        return mineSprite

    @staticmethod
    def flag(x: int, y: int, scale: float = 1.0, flagColor: str = "red") -> Group:
        pole = Line(
            x,y,
            x,y+(100*scale),
            lineWidth=13*scale
        )
        
        flag = Polygon(
            x+(pole.lineWidth/2)*scale,y,
            x+(pole.lineWidth/2)*scale,y+((pole.y2/5)*scale),
            x+(50*scale),y+((pole.y2/10)*scale),
            fill=flagColor
        )
        
        flagSprite = Group( flag, pole )
        return flagSprite
