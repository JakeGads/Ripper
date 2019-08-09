import ImageCaptureSetup
import applyOCR

from subprocess import call
try:
    import pyscreenshot as ImageGrab
    import pyautogui
except:
    try:
        call('python3 -m pip install -r requirments.txt')
    except:
        call('python -m pip install -r requirments.txt')

    try:
        import pyscreenshot as ImageGrab
        import pyautogui
    except:
        print('Error finding packages please run the following command\n\tpip install -r requirments.txt\n\nNote on Linux system PIL must be downloaded through a package manager')


def build():
    box = ImageCaptureSetup.findGoodBox()
    tup = ImageCaptureSetup.findCommand() 
	
    try:    
        call('cd temp')
        call('rm *')
        call('cd ..')
        call('rmdir temp')
    except:
        None
    
    call('mkdir temp')
    call('cd temp')
    counter = 0
	
    while(doubleCheck()):
        capture(box, counter)
        counter += 1
        if tup[0]: tup[1](tup[2][0], tup[2][1])
       else: tup[1](tup[2])    

	done()

def doubleCheck():
    None


def capture(box, counter):
    im = ImageGrab.grab(bbox=box)
	im.save('temp/Page{num}.jpeg'.format(num=counter))
	
def done():
	#bound the pdf
	None

def main():
    None
    