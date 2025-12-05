import threading
import time



def cpu_task():
    total = 0
    for i in range(50000):
        total += 1
    
    return total

def run_single_thread():
    start = time.time()

    for i in range(4):
        cpu_task()

    end = time.time()
    print(f"Single-thread total time: {end - start:.4f} seconds")

def run_multi_thread():
    start = time.time()

    Threads = []

    for i in range(4):
        t = threading.Thread(target=cpu_task)
        Threads.append(t)

    for t in Threads:
        t.start()

    for t in Threads:
        t.join()

    end = time.time()
    print(f"Multi-thread total time: {end - start:.4f} seconds")

def main():

    print("Running single Threaded version")
    run_single_thread()

    print("Running Multi-Threaded version")
    run_multi_thread()

if __name__ == "__main__":
    main()