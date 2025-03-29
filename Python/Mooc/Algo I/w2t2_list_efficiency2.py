import time

def adding(my_list, numbers):
    for i in numbers: my_list.append(i)
    return my_list

def deleting(my_list, numbers):
    for i in numbers: my_list.pop(0)
    return my_list

numbers = [_ for _ in range(10**5)]
my_list = []
start_time = time.perf_counter()
result = adding(my_list, numbers)
end_time = time.perf_counter()

print(f"1: {end_time - start_time:.6f} s")

start_time = time.perf_counter()
result = deleting(my_list, numbers)
end_time = time.perf_counter()

print(f"2: {end_time - start_time:.6f} s")

