class PermutationTracker:
    def __init__(self):
        self.numbers = {}
        self.maximum = 0
        self.duplicate = False

    def append(self, number):
        if number in self.numbers:
            self.duplicate = True
        self.numbers[number] = number
        self.maximum = max(number, self.maximum)

    def check(self):
        if self.duplicate: return False
        return len(self.numbers) == self.maximum

if __name__ == "__main__":
    tracker = PermutationTracker()

    tracker.append(1)
    print(tracker.check()) # True

    tracker.append(4)
    print(tracker.check()) # False

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(3)
    print(tracker.check()) # True

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(5)
    print(tracker.check()) # False