from collections import defaultdict

def count_splits(numbers):
    n = len(numbers)
    if n < 2: return 0
    left_freq = {}
    right_freq = {}
    right_count = 0
    left_count = 0
    count = 0

    for num in numbers:
        if num not in right_freq:
            right_freq[num] = 0
            right_count += 1
        right_freq[num] += 1

    if right_count == n: return 0

    for i in range(n - 1):
        num = numbers[i]
        if num not in left_freq:
            left_freq[num] = 0
            left_count += 1
        left_freq[num] += 1

        right_freq[num] -= 1
        if right_freq[num] == 0:
            right_count -= 1
            del right_freq[num]
        
        if left_count == right_count and left_freq.keys() == right_freq.keys():
            count += 1
    return count

if __name__ == "__main__":
    print(count_splits([1, 1, 1, 1])) # 3
    print(count_splits([1, 1, 2, 1])) # 0
    print(count_splits([1, 2, 1, 2])) # 1
    print(count_splits([1, 2, 3, 4])) # 0
    print(count_splits([1, 2, 1, 2, 1, 2])) # 3
    print(count_splits([3, 3, 5])) # 0

    numbers = [1, 2] * 10**5
    print(count_splits(numbers)) # 199997
    numbers = list(range(1, 10**5 + 1)) * 2
    print(count_splits(numbers)) # 1