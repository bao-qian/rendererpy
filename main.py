from glutwindow import GlutWindow
import cProfile

import pstats

# if __name__ == '__main__':
def main():
    width = 400
    height = 300
    title = b'Screen.py'

    win = GlutWindow(width, height, title)
    win.run()

if __name__ == '__main__':
    main()