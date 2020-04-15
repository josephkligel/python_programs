import threading
import os

def pushing():
    print('Waiting')
    event.wait()
    os.system('zigjag')

thread = threading.Thread(target=pushing)
x = os.system('gitPushAll.py')
if (x == 'username:'):
    event.set()
