class DistanceTracker:
    def __init__(self):
        self.positions = {}
        self.distance_sums = {}
        self.cumulative_sums = {}
        self.index = 0

    def append(self, number):
        if number not in self.positions:
            self.positions[number] = []
            self.distance_sums[number] = 0
            self.cumulative_sums[number] = 0

        occurences = len(self.positions[number])
        if occurences > 0:
            last_sum = self.cumulative_sums[number]
            self.distance_sums[number] += occurences * self.index - last_sum
        
        self.positions[number].append(self.index)
        self.cumulative_sums[number] += self.index
        self.index += 1

    def sum(self, number):
        return self.distance_sums.get(number, 0)

if __name__ == "__main__":
    tracker = DistanceTracker()
    total = 0
    for i in range(10**5):
        tracker.append(1)
        total += tracker.sum(1)
    print(total) # 4166749999583325000