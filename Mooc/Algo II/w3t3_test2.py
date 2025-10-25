from collections import deque
import heapq
import time
import random

temp = deque()

def test1(nums:list):
    temp = sorted(nums)
    limit = len(temp)//10
    return sum(temp[:limit])

def test2(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap,num)
    limit = len(nums)//10
    total = 0
    for _ in range(limit):
        total += heapq.heappop(heap)
    return total

def test3(nums):
    heap = nums[:]
    heapq.heapify(nums)
    limit = len(nums)//10
    total = 0
    for _ in range(limit):
        total += heapq.heappop(heap)
    return total
  
random.seed(1337)
nums = [random.randint(1, 10**9) for _ in range(10**7)]

start_time = time.perf_counter()
test1(nums)
end_time = time.perf_counter()
print(f"1. time: {end_time - start_time:.6f} s")

start_time = time.perf_counter()
test2(nums)
end_time = time.perf_counter()
print(f"2. time: {end_time - start_time:.6f} s")


start_time = time.perf_counter()
test3(nums)
end_time = time.perf_counter()
print(f"3. time: {end_time - start_time:.6f} s")

