import webbrowser, sys
import pyperclip

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paster()

webbrowser.open(f'https://www.google.com/maps/place/{address}')
