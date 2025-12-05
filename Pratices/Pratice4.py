import threading
import time
from queue import Queue

q = Queue()

def Producer():
    for i in range(20):
        print(f"Producer : Producing {i}")
        q.put(i)
        time.sleep(1)
    q.put(None)

def Consumer():
    for i in range(20):
        data = q.get()

        if data is None:
            print("Producer Queue is None!")
            break
        print(f"Consumer : Counsuming {data}")
        time.sleep(1)

    q.task_done()


Producer1 = threading.Thread(target=Producer)
Consumer1 = threading.Thread(target=Consumer)

Producer1.start()
Consumer1.start()

Producer1.join()
Consumer1.join()