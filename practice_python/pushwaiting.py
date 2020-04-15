import threading
import os
import sys

def pushing():
    os.system('gitPushAll.py')
    event.wait()
    print('zigjag')

thread = threading.Thread(target=pushing)
if (sys.stdin == "Username for 'https://github.com:'"):
    event.set()
