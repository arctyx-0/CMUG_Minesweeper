import os
import sys

from dataclasses import dataclass
from cmu_graphics import rgb

class Utils:
    def restart():
        if sys.platform == 'darwin':
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif sys.platform == 'win32':
            os.execv(sys.executable, ['python'] + sys.argv)

@dataclass
class Colors:
    gray       = rgb(175,175,175)
    darkGray   = rgb(100,100,100)
    darkerGray = rgb(80,80,80)

    red = rgb(245,20,30)

    # number colors
    class number:
        one   = rgb(3,119,252)
        two   = rgb(30,227,62)
        three = rgb(227,30,30)
        four  = rgb(45,19,161)
        five  = rgb(140,14,14)
        six   = rgb(21,149,161)
        seven = rgb(133,29,171)
        eight = rgb(112,112,112)
