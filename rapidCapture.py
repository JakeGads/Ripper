import ImageCaptureSetup
import applyOCR

def build():
    box = ImageCaptureSetup.findGoodBox()
    tup = ImageCaptureSetup.findCommand() 
    
    while(doubleCheck()):
        capture(box)
        if tup[0]: tup[1](tup[2][0], tup[2][1])
        else: tup[1](tup[2])    


def doubleCheck():
    None


def capture(box):
    None    

def main():
    None
    