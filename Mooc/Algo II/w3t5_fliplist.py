from collections import deque

class FlipList:
    def __init__(self):
        self.deque = deque()
        self.flipped = False

    def __repr__(self):
        if self.flipped: return str(list(reversed(self.deque)))  
        else: return str(list(self.deque)) 

    def add_first(self, x):
        if self.flipped:
            self.deque.append(x)
        else:
            self.deque.appendleft(x)

    def add_last(self, x):
        if self.flipped: self.deque.appendleft(x)
        else: self.deque.append(x)

    def flip(self):
        self.flipped = not self.flipped

if __name__ == "__main__":
    numbers = FlipList()

    numbers.add_last(1)
    numbers.add_last(2)
    numbers.add_last(3)
    print(numbers) # [1, 2, 3]

    numbers.add_first(4)
    print(numbers) # [4, 1, 2, 3]

    numbers.flip()
    print(numbers) # [3, 2, 1, 4]

    numbers.add_last(5)
    print(numbers) # [3, 2, 1, 4, 5]