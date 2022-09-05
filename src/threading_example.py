import threading as t
import time

def f(barrier):
    print("f start: ", time.time())
    time.sleep(2)
    print("f end: ", time.time())
    barrier.wait()


def g(barrier):
    print("g start: ", time.time())
    time.sleep(2)
    print("g end: ", time.time())
    barrier.wait()

b = t.Barrier(3, timeout=5)

t1 = t.Thread(target=f, args=(b,))
t2 = t.Thread(target=g, args=(b,))
t1.start()
t2.start()
b.wait()
