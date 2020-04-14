import threading
import time

semaphore = threading.BoundedSemaphore(value=5)
def access(threadNumber):
    print(f"{threadNumber}: Trying Access...")
    semaphore.acquire()
    print(f'{threadNumber}: Access Granted!')
    print(f'{threadNumber}: Waiting 5 seconds...')
    time.sleep(5)
    semaphore.release()
    print(f'{threadNumber}: Releasing!')

for threadNumber in range(10):
    t = threading.Thread(target=access, args=(threadNumber,))
    t.start()
