import math

class Comparer:
    def __init__(self, numbers):
        self.numbers = numbers
        self.counter = 0
        n = len(self.numbers)
        self.bound = n * math.floor(math.log2(n))

    def list_size(self):
        return len(self.numbers)

    def smaller(self, a, b):
        self.counter += 1
        if self.counter > self.bound:
            raise RuntimeError("too many comparisons")
        return self.numbers[a] < self.numbers[b]

def find_list(comparer):
    size = comparer.list_size()
    indices = list(range(size))

    def merge_sort(arr):
        if len(arr) <= 1: return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    
    def merge(left, right):
        sorted = []
        i,j = 0,0

        while i < len(left) and j < len(right):
            if comparer.smaller(left[i], right[j]):
                sorted.append(left[i])
                i += 1
            else:
                sorted.append(right[j])
                j += 1
        sorted.extend(left[i:])
        sorted.extend(right[j:])
        return sorted
    
    sorted_indices = merge_sort(indices)
    result = [0] * size
    for value, i in enumerate(sorted_indices, start=1):
        result[i] = value
    return result

if __name__ == "__main__":
    comparer = Comparer([3, 1, 2, 4])
    numbers = find_list(comparer)
    print(numbers) # [3, 1, 2, 4]

    comparer = Comparer([1, 6, 2, 5, 3, 4])
    numbers = find_list(comparer)
    print(numbers) # [1, 6, 2, 5, 3, 4]