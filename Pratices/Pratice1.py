import threading
import time

def download(i, ThreadTime):
    startTime = time.time()
    print("File {} is downloading...".format(i))
    time.sleep(2)
    print("File {} is downloaded".format(i))
    endTime = time.time()
    ThreadTime[i] = endTime - startTime

ThreadTime = [0] * 6
threads = []

for i in range(1, 6):
    t = threading.Thread(target=download, args=(i, ThreadTime,))
    threads.append(t)
    t.start()

for i in range(1, 6):
     t.join()

print("Total time to complete downloading: {}".format(sum(ThreadTime)))



