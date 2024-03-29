import os
import subprocess
import time
from random import randint


import applyOCR
import ImageCaptureSetup

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

    file = open('previous_setup.txt', 'w+')
    file.write(str(box))
    file.close()

    clear()

    counter = 0

    print("You have 10 seconds to configure everything ... good luck my guy")
    time.sleep(10)

    if pages:
        for i in range(pages):
            time.sleep(randint(0, wait))
            capture(box, counter)
            counter += 1
            print('captured {i}'.format(i=i))
            if tup[0]:
                tup[1](tup[2][0], tup[2][1])
            else:
                tup[1](tup[2])
    else:
        sameImage = True

        while sameImage:
            time.sleep(randint(0, wait))
            capture(box, counter)
            counter += 1
            if tup[0]:
                tup[1](tup[2][0], tup[2][1])
            else:
                tup[1](tup[2])
            print('captured {}'.format(counter))
            sameImage = doubleCheck(counter)

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
    from fpdf import FPDF
    import glob

    if '.pdf' not in name:
        name += ".pdf"

    pdf = FPDF()
    # imagelist is the list with all image filenames

    imagelist = [f for f in glob.glob("*.jpg")]

    counter = 0
    # adds the image to a new page and then deletes the image from the hardrive
    for image in imagelist:
        pdf.add_page()
        pdf.image(image)
        os.remove(image)
        print("PAGE {} ADDED".format(counter))
        counter += 1
        
    pdf.output(name, "F")


if __name__ == "__main__":  
    name = input("output file name: \t")
    wait = int(input("time pause between captures (seconds)\t"))
    pages = None
    try:
        pages = int(input("How many pages\t"))
    except:
        None
    
    build(name, wait, pages=pages)
