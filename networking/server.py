import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen()
print('listening on port 9999...')

while True:
    client, address = s.accept()
    print(f'Connected to {address}')
    message = 'Hello Client!'
    client.send(message.encode('ascii'))
    client.close()
