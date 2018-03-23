import numpy as np
import time as tm

t = tm.time()
arr = np.arange(1000000000, dtype=np.float64)

print('Time took to make 1B element of 64Bit float is: \t', tm.time() - t)