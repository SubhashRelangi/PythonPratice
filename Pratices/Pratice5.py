import threading

Progress = [0]

lock = threading.Lock()

def Worker(name, Progress):
    for i in range(10000):
        with lock:
            Progress[0] += 1

    print(f"Worker {name}: Finished.")

def main():

    Threads = []

    for i in range(5):
        t = threading.Thread(target=Worker, args=(f"Worker{i}", Progress,))
        Threads.append(t)

    for t in Threads:
        t.start()

    for t in Threads:
        t.join()

    print("The Total progress of the Workers is: {}".format(Progress))

if __name__ == "__main__":
    main()

