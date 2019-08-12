import ImageCaptureSetup
import applyOCR
import os
import time
from random import randint
from subprocess import call


try:
    import pyscreenshot as ImageGrab
    import pyautogui
    import cv2
    import numpy as np
    import img2pdf
except:
    try:
        call("python3 -m pip install -r requirments.txt --user")
    except:
        call("python -m pip install -r requirments.txt --user")

    try:
        import pyscreenshot as ImageGrab
        import pyautogui
        import cv2
        import numpy as np
    except:
        print(
            "Error finding packages please run the following command\n\tpip install -r requirments.txt\n\nNote on Linux system PIL must be downloaded through a package manager"
        )


def build(name, wait):
    box = ImageCaptureSetup.findGoodBox()
    tup = ImageCaptureSetup.findCommand()

    try:
        call("cd temp")
        call("rm *")
        call("cd ..")
        call("rmdir temp")
    except:
        None

    call("mkdir temp")
    call("cd temp")
    counter = 0

    while doubleCheck(counter):
        time.sleep(randint(0,wait))
        capture(box, counter)
        counter += 1
        if tup[0]:
            tup[1](tup[2][0], tup[2][1])
        else:
            tup[1](tup[2])

    generatePDF(name)


def doubleCheck(counter):
    try:
        # Loads both images into RAM
        new = cv2.imread("{counter}.jpg".format(counter=counter))
        previous = cv2.imread(
            "{counter_minus_one}.jpg".format(counter_minus_one=counter - 1)
        )

        # checks to see if they are the same shape
        if new.shape == previous.shape:
            print("The images have same size and channels")
            # calculates all of the color differences
            difference = cv2.subtract(new, previous)

            # splits all of the differnces into rgb values
            b, g, r = cv2.split(difference)

            # compares the RGB valuse, if they are the same then the image is the same and it exits the loop
            if (
                cv2.countNonZero(b) == 0
                and cv2.countNonZero(g) == 0
                and cv2.countNonZero(r) == 0
            ):
                return False
            else:
                return True
        else:
            return True

    except:
        return True


def capture(box, counter):
    im = ImageGrab.grab(bbox=box)
    im.save("Page{num}.jpg".format(num=counter))


def generatePDF(name):
    if '.pdf' not in name:
        name += '.pdf'
    
    with open (name, 'wb') as f:
        f.write(img2pdf.convert([i for i in os.listdir('temp') if i.endswith(".jpg")]))


if __name__ == "__main__":
    name = input('output file name: \t')
    wait = int(input('time pause between captures (seconds)'))
    build(name, wait)