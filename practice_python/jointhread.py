import threading

def function():
    for x in range(500000):
        print('Hello world!')

t1 = threading.Thread(target=function)
t1.start()
t1.join(5)
print('This is the end!')
