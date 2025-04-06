import itertools


def count_combinations(cards, target):
    count = 0
    for i in range(1, len(cards)+1):
        for combination in itertools.combinations(cards, i):
            if check_sum(combination, target): count += 1
    return count

def check_sum(cards, target):
    if sum(cards) == target: return True
    return False

if __name__ == "__main__":
    print(count_combinations([2, 1, 4, 6], 6)) # 2
    print(count_combinations([1, 1, 1, 1], 2)) # 6
    print(count_combinations([2, 1, 4, 6], 15)) # 0
    print(count_combinations([1], 1)) # 1
    print(count_combinations([1, 2, 3, 4, 5], 5)) # 3
    print(count_combinations([1, 1, 4, 1, 1], 4)) # 2
    print(count_combinations([1] * 10, 5)) # 252