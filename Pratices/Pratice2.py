import threading
import time

balance = [100]
lock = threading.Lock()

def withdraw(n, balance, lock):
    for i in range(10000):
        with lock:
            balance[0] -= 1


t1 = threading.Thread(target=withdraw, args=(1, balance, lock,))
t2 = threading.Thread(target=withdraw, args=(2, balance, lock,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Thread balance is: {}".format(balance))