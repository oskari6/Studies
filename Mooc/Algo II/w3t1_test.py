from collections import deque
import time

temp = deque()

start_time = time.perf_counter()
[temp.append(i) for i in range(10**5)]
end_time = time.perf_counter()
print(f"1. time: {end_time - start_time:.6f} s")

start_time = time.perf_counter()
[temp.popleft() for i in range(10**5)]
end_time = time.perf_counter()
print(f"2. time: {end_time - start_time:.6f} s")

