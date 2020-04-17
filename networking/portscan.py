import socket

target = '10.0.0.56'

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect((target, port))
        return True
    except:
        return False

for x in range(1, 501):
    if(portscan(x)):
        print(f'Port {x} is open!')
    else:
        print(f'Port {x} closed')
