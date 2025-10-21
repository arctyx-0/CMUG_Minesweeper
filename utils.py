import os
import sys

class Utils:
    def restart():
        if sys.platform == 'darwin':
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif sys.platform == 'win32':
            os.execv(sys.executable, ['python'] + sys.argv)
