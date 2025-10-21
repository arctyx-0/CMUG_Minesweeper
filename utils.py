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
