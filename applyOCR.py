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