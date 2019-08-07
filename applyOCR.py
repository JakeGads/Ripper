from subprocess import call
from sys import platform
try:
    try:
        from PIL import Image
    except ImportError:
        import Image
    
    import pytesseract
except:
    try:
        try:
            call('python3 -m pip install -r requirments.txt')
        except:
            call('python -m pip install -r requirments.txt')
    except:
        print('We have encountered an unexpected error\n\nopen up a terminal window and enter the following cd into the folder and enter the following command\n\tpip install -r requirments.txt')

    try:
        from PIL import Image
    except ImportError:
        import Image
    
    import pytesseract

def ocr_core(filename):
    return pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image

'''
TODO this a suprise that will help us latter

from pdf2image import convert_from_path
imgs = convert_from_path('path/to/your/file.pdf', 200)

and imgs is a list of your pdf's pages as PIL image
'''