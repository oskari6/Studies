import random
import time

# implementation 1
def count_even_1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

# implementation 2
def count_even_2(numbers):
    return sum(x % 2 == 0 for x in numbers)

random.seed(1337)
numbers = [random.randint(1, 100) for _ in range(10**7)]

start_time = time.perf_counter()  # High-precision timer
result = count_even_1(numbers)
end_time = time.perf_counter()  # High-precision timer

print("result:", result)
print(f"1. time: {end_time - start_time:.6f} s")

start_time = time.perf_counter()  # High-precision timer
result = count_even_2(numbers)
end_time = time.perf_counter()  # High-precision timer

print("result:", result)
print(f"2. time: {end_time - start_time:.6f} s")

