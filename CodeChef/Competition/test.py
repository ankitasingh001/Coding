import numpy as np
import time

start_time = time.time()
count_arr = np.zeros(10000,int)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
arr = [1]*10000
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
j=0
for i in count_arr:
    j+=1
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
j=0
for i in arr:
    j+=1
print("--- %s seconds ---" % (time.time() - start_time))