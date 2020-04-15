import threading
import os

def pushing():
    print('Waiting')
    event.wait()
    os.system('exit')

thread = threading.Thread(target=pushing)
x = os.system('gitPushAll.py')
if (x == "Username for 'https://github.com:'"):
    event.set()
