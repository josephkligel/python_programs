from queue import Queue
import socket
import threading

target = '10.0.0.236'

q = Queue()
for x in range(1, 501):
    q.put(x)

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect((target, port))
        return True
    except:
        return False

def worker():
    while True:
        port = q.get()
        if portscan(port):
            print(f'Port {port} is open!')
        else:
            print(f'Port {port} is closed.')

for x in range(30):
    t = threading.Thread(target=worker)
    t.start()
