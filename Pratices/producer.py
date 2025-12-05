from multiprocessing import shared_memory
import numpy as np

arr = np.arange(10, dtype=np.int64)
nbytes = arr.nbytes

shm = shared_memory.SharedMemory(create=True, size=nbytes)
buf = np.ndarray(arr.shape, dtype=arr.dtype, buffer=shm.buf)
buf[:] = arr[:]    # copy into shared memory

print("SHM_NAME=", shm.name)   # send this name to consumer, e.g. IPC, environment, file
# keep process alive so consumer can attach (for demo)
input("Press Enter to cleanup and exit...\n")

shm.close()
shm.unlink()  # free the OS resource
