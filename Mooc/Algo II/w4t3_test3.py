import random
import time

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None
        self.max_depth = -1

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            self.max_depth = max(self.max_depth, 0)
            return
        node = self.root
        height = 0
        while True:
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    self.max_depth = max(self.max_depth, height+1)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    self.max_depth = max(self.max_depth, height+1)
                    return
                node = node.right
            height += 1

    def height(self):
        return self.max_depth
 
nums = [_ for _ in range(1,1001)]
random.seed(1337)
numbers = TreeSet()

start_time = time.perf_counter()
for num in nums:
    numbers.add(num)
end_time = time.perf_counter()
print(f"1. time: {end_time - start_time:.6f} s")

random.shuffle(nums)
numbers = TreeSet() 
start_time = time.perf_counter()
for num in nums:
    numbers.add(num)
end_time = time.perf_counter()
print(f"2. time: {end_time - start_time:.6f} s")
