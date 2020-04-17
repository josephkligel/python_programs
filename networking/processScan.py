from multiprocessing import Process
import socket
import queue

target = '10.0.0.56'
q = queue.Queue()
for i in range(1, 501):
    q.put(i)

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect((target, port))
        return True
    except Exception as exc:
        print(exc)
        return False

def worker():
    port = q.get()
    if portscan(port):
        print(f'Port {port} is open!')

for x in range(0, 30):
    process = Process(target=worker)
    process.start()
