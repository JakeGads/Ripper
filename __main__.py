from subprocess import call
try:
    import pyscreenshot as ImageGrab
except:
    try:
        call('python3 -m pip install -r requirments.txt')
    except:
        call('python -m pip install -r requirments.txt')

    try:
        import pyscreenshot as ImageGrab
    except:
        print('Error finding packages please run the following command\n\tpip install -r requirments.txt\n\nNote on Linux system PIL must be downloaded through a package manager')


def findGoodBox():
    x1 = 0
    y1 = 0
    x2 = 1920
    y2 = 1080
    
    box = (x1, y1, x2, y2)

    not_good = True
    while(not_good):
        im = ImageGrab.grab(bbox=box)
        im.save('NewShot.jpeg')

        if input('if this shot is good enter y:\t') == 'y':
            not_good = False
        else:

            print('''
            Current Values
                x1 = {x1},\t\t\t min val = 0
                y1 = {y1},\t\t\t min val = 0
                x2 = {x2},\t\t\t max val = 1920
                y2 = {y2},\t\t\t max val = 1080
                Min / Max values are based on the standard screen sizes
            '''.format(x1=x1, y1=y1, x2=x2, y2=y2))

            x1 = int(input('X1: Current Val: {}\tNew Val: '.format(x1)))
            y1 = int(input('Y1: Current Val: {}\tNew Val: '.format(y1)))
            x2 = int(input('X2: Current Val: {}\tNew Val: '.format(x2)))
            y2 = int(input('Y2: Current Val: {}\tNew Val: '.format(y1)))

            box = (x1, y1, x2, y2)
            
    return box

if __name__ == "__main__":
    box = findGoodBox()