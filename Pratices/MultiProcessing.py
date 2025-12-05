# from multiprocessing import Process
# import time

# def print_numbers(name):
#     for i in range(1, 6):
#         print(f"{name} -> {i}")
#         time.sleep(1)   # slow it down so you can see both processes running

# if __name__ == "__main__":
#     # Create two processes
#     p1 = Process(target=print_numbers, args=("Process 1",))
#     p2 = Process(target=print_numbers, args=("Process 2",))

#     # Start processes
#     p1.start()
#     p2.start()

#     # Wait for both to finish
#     p1.join()
#     p2.join()

#     print("Both processes completed.")


# from multiprocessing import Process
# import time

# def cpu_task():
#     # Heavy CPU work (big loop)
#     total = 0
#     for i in range(10_000_000):
#         total += i
#     return total

# if __name__ == "__main__":
#     start = time.time()

#     # Create two processes
#     p1 = Process(target=cpu_task)
#     p2 = Process(target=cpu_task)

#     # Start both processes (run in parallel)
#     p1.start()
#     p2.start()

#     # Wait for both to complete
#     p1.join()
#     p2.join()

#     end = time.time()

#     print(f"Total multiprocessing time: {end - start:.2f} seconds")


# from multiprocessing import Pool    
# import time


# def square(n):
#     total = 0
#     for i in range(50000):
#         total += i * i
#         return n * n
    
# if __name__ == "__main__":
    
#     numbers = [1, 2, 3, 4, 5]

#     start = time.time()

#     with Pool(4) as p:
#         result = p.map(square, numbers)
    
#     end = time.time()

#     print(f"Results: {result}")
#     print(f"Time taken to complete the process: {end - start:.2f} seconds")


# from multiprocessing import Pool
# import time
# import random

# def work(n):
#     t = random.randint(1, 3)
#     print(f"Task {n} started, will take {t} sec...")
#     time.sleep(t)
#     print(f"Task {n} finished.")
#     return n * n  # return square

# def collect_result(result):
#     print("Collected result:", result)

# if __name__ == "__main__":
#     with Pool(4) as p:
#         results = []

#         for i in range(1, 6):
#             r = p.apply_async(work, args=(i,), callback=collect_result)
#             results.append(r)

#         # Wait for all tasks to finish
#         for r in results:
#             r.wait()

#     print("All tasks completed.")

# from multiprocessing import Process, Queue

# def producer(q):
#     print("Producer sending message to the consumer.")
#     q.put("Hello from producer")

# def consumer(q):
#     msg = q.get()
#     print("Consumer received:", msg)

# if __name__ == "__main__":
#     q = Queue()

#     p1 = Process(target=producer, args=(q,))
#     p2 = Process(target=consumer, args=(q,))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

# from multiprocessing import Process, Pipe

# def sender(conn):
#     conn.send("Hello from child")
#     conn.close()

# def receiver(conn):
#     msg = conn.recv()
#     print("Parent received:", msg)

# if __name__ == "__main__":
#     parent_conn, child_conn = Pipe()

#     p = Process(target=sender, args=(child_conn,))
#     p.start()

#     print("Parent waiting...")
#     data = parent_conn.recv()
#     print("Parent got:", data)
#     parent_conn.send("Hello child this is parent.")

#     p.join()


# producer_consumer.py
from multiprocessing import Process, Lock
from multiprocessing import shared_memory
import numpy as np
import time

def producer(name, shape, dtype, lock):
    # create shared memory
    nbytes = np.prod(shape) * np.dtype(dtype).itemsize
    shm = shared_memory.SharedMemory(create=True, size=nbytes)
    print("Producer created shm name:", shm.name)

    arr = np.ndarray(shape, dtype=dtype, buffer=shm.buf)
    # write data
    with lock:
        arr[:] = np.arange(arr.size).reshape(shape)
    # keep alive for consumer
    time.sleep(2)

    # cleanup (producer still must close; do not unlink if consumer still using)
    shm.close()
    # unlink only when you are sure nobody else will attach
    shm.unlink()

def consumer(shm_name, shape, dtype, lock):
    # attach to existing shared memory by name
    shm = shared_memory.SharedMemory(name=shm_name)
    arr = np.ndarray(shape, dtype=dtype, buffer=shm.buf)
    # read safely
    with lock:
        print("Consumer read slice:", arr[0:5])
    shm.close()

if __name__ == "__main__":
    shape = (1000,)
    dtype = np.int64
    lock = Lock()
    # We start producer to create and register the name
    p = Process(target=consumer, args=('psm_1debfdfb', shape, dtype, lock))
    p.start()
    p.join()  # In real cases you'd coordinate differently to get the name; this is simplified.

