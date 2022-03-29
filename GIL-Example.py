import time
from threading import Thread

count = 50000000

def countdown(n):
    while n>0:
        n -= 1

# with single thread

if __name__ == "__main__":
    start = time.time()
    countdown(count)
    ended = time.time()
    print('Time taken in seconds :', ended - start)

# with multiple threads

t1 = Thread(target=countdown, args=(count//2,))
t2 = Thread(target=countdown, args=(count//2,))

if __name__ == "__main__":
    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    ended = time.time()

    print('Time taken in seconds :', ended - start)