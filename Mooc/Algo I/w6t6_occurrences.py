class OccurrenceTracker:
    def __init__(self):
        self.numbers = {}
        self.occurences = {}

    def append(self, number):
        if number in self.numbers:
            old_count = self.numbers[number]
            self.numbers[number] += 1
            new_count = self.numbers[number]

            if old_count in self.occurences:
                self.occurences[old_count] -= 1
                if self.occurences[old_count] == 0: del self.occurences[old_count]
        else:
            self.numbers[number] = 1
            new_count = 1
        if new_count in self.occurences: self.occurences[new_count] += 1
        else: self.occurences[new_count] = 1
            

    def count(self):
        return len(self.occurences)

if __name__ == "__main__":
    tracker = OccurrenceTracker()

    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    print(tracker.count()) # 2

    tracker.append(2)
    tracker.append(3)
    print(tracker.count()) # 1

    tracker.append(2)
    tracker.append(3)
    tracker.append(3)
    print(tracker.count()) # 3