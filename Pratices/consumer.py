from multiprocessing import shared_memory
import numpy as np
import os
import sys

shm_name = os.environ.get("SHM_NAME") or sys.argv[1]  # get name somehow
# attach
shm = shared_memory.SharedMemory(name=shm_name)
# interpret bytes as numpy array (you must know shape/dtype)
arr = np.ndarray((10,), dtype=np.int64, buffer=shm.buf)
print("Got array:", arr[:])
shm.close()
