import random
import time

def find_mode(numbers):
    count = {}
    mode = (0, 0)

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1

        mode = max(mode, (count[x], x))

    return mode[1]

def find_mode_2(numbers):
    numbers.sort()
    most = numbers[0]
    count = 1
    max_count = 1
    previous = numbers[0]
    for i in range(1,(len(numbers))):
        if numbers[i] == previous:
            count += 1
        else:
            count = 1
            previous = numbers[i]
        if count > max_count:
            max_count = count
            most = numbers[i]
    return most

if __name__ == "__main__":
    random.seed(1337)
    numbers = [random.randint(1, 1000) for _ in range(10**7)]

    start_time = time.perf_counter()
    print(find_mode(numbers))
    end_time = time.perf_counter()
    print(f"1: {end_time - start_time:.6f} s")
    
    start_time = time.perf_counter()
    find_mode_2(numbers)
    end_time = time.perf_counter()
    print(f"2: {end_time - start_time:.6f} s")
