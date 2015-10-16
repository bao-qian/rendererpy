from glutwindow import GlutWindow


def main():
    width = 300
    height = 300
    title = b'Screen'

    win = GlutWindow(width, height, title)
    win.run()


if __name__ == '__main__':
    main()
