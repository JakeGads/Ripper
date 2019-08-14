import os
import subprocess
import time
from random import randint


import applyOCR
import ImageCaptureSetup

os.system("pip install -r requirments.txt --user")

import cv2
import img2pdf
import numpy as np
import pyautogui
import pyscreenshot as ImageGrab



def clear():
    if os.name == "Windows":
        os.system("cls")
    else:
        os.system("clear")

clear()

def build(name, wait, pages=None):
    box = ImageCaptureSetup.findGoodBox()
    tup = ImageCaptureSetup.findCommand()

    """
    try:
        output = str(subprocess.check_output("cd temp", shell=True))
        input(output)
        
        if 'no such file' in output:
            None
        else:
            os.system('cd temp')
            os.system("rm *")
            os.system("cd ..")
            os.system("rmdir temp")
    except:
        None
    """

    os.system("mkdir temp")
    os.system('rm temp/*')
    clear()

    counter = 0

    sameImage = True

    while sameImage:
        time.sleep(randint(0, wait))
        capture(box, counter)
        counter += 1
        if tup[0]:
            tup[1](tup[2][0], tup[2][1])
        else:
            tup[1](tup[2])

        sameImage = doubleCheck(counter)

    generatePDF(name)


def doubleCheck(counter):
    try:
        # Loads both images into RAM
        new = cv2.imread("temp/{counter}.jpg".format(counter=counter))
        previous = cv2.imread(
            "temp/{counter_minus_one}.jpg".format(counter_minus_one=counter - 1)
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
    im.save("temp/Page{num}.jpg".format(num=counter))


def generatePDF(name):
    if ".pdf" not in name:
        name += ".pdf"

    with open(name, "wb") as f:
        f.write(img2pdf.convert([i for i in os.listdir("temp") if i.endswith(".jpg")]))


if __name__ == "__main__":
    name = input("output file name: \t")
    wait = int(input("time pause between captures (seconds)\t"))
    pages = int(input("How many pages\t"))
    build(name, wait, pages=pages)
