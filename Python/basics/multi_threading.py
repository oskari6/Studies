import threading
import time

lock = threading.Lock()
counter = 0

def print_numbers():
    global counter
    for i in range(5):
        with lock:
            print(counter + i)
            time.sleep(1)
            counter += 1

def print_letters():
    for char in "ABCDE":
        print(char)
        time.sleep(1)

threads = [threading.Thread(target=print_numbers) for _ in range(10)]
thread2 = threading.Thread(target=print_letters)

for t in threads:
    t.start()
thread2.start()

for t in threads:
    t.join()
thread2.join()

print("done")