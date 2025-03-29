class MaxList:
    def __init__(self):
        self.numbers = []
        self.maximum = 0

    def append(self, number):
        self.numbers.append(number)
        self.maximum = max(self.maximum, number)

    def max(self):
        return self.maximum

if __name__ == "__main__":
    numbers = MaxList()

    numbers = MaxList()
    numbers.append(1)
    print(numbers.max())
    numbers.append(3)
    print(numbers.max())
    numbers.append(1)
    print(numbers.max())
