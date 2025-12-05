import threading
import time

def squares(num):
    print(f"The squares of this {num} is: {num*num}")
    time.sleep(1)

def cube(num):
    print(f"The cube of the {num} is: {num*num*num}")
    time.sleep(1)

t1 = threading.Thread(target=squares, args=(4,))
t2 = threading.Thread(target=cube, args=(5,))

t1.start()
t2.start()
t1.join()
t2.join()
