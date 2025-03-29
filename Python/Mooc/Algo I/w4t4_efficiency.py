import time
import random

def count_rounds(numbers):
    n = len(numbers)
    pos = [0] * (n+1)

    for i in range(n):
        pos[numbers[i]] = i

    rounds = 1
    for number in range(2, n+1):
        if pos[number] < pos[number - 1]:
            rounds += 1

    return rounds

def count_rounds_2(numbers):
    n = len(numbers)
    
    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i
        
    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1

    return rounds

def count_rounds_3(numbers):
    n = len(numbers)
    
    pos = [0] * (n+1)
    for i, x in enumerate(numbers):
        pos[x] = i
        
    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1

    return rounds

if __name__ == "__main__":
    random.seed(1337)
    numbers = random.sample(range(1, 10**7+1), 10**7)

    start_time = time.perf_counter()
    print(count_rounds(numbers))
    end_time = time.perf_counter()
    print(f"1: {end_time - start_time:.6f} s")
    
    start_time = time.perf_counter()
    print(count_rounds_2(numbers))
    end_time = time.perf_counter()
    print(f"2: {end_time - start_time:.6f} s")
    
    start_time = time.perf_counter()
    print(count_rounds_3(numbers))
    end_time = time.perf_counter()
    print(f"3: {end_time - start_time:.6f} s")
    

