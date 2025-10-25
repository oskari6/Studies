import itertools


def check_sum(numbers):
    total_sum = sum(numbers)

    if total_sum % 2 != 0: return False
        
    target = total_sum // 2

    for i in range(1, len(numbers)+1):
        for combination in itertools.combinations(numbers, i):
            if sum(combination) == target: return True

    return False

if __name__ == "__main__":
    print(check_sum([1, 2, 3, 4])) # True
    print(check_sum([1, 2, 3, 5])) # False
    print(check_sum([0])) # True
    print(check_sum([2, 2])) # True
    print(check_sum([2, 4])) # False
    print(check_sum([1, 5, 6, 3, 5])) # True
    print(check_sum([1, 5, 5, 3, 5])) # False
    print(check_sum([10**9, 2*10**9, 10**9])) # True
    print(check_sum([1, 1, 1, 1, 1, 1, 1, 1, 1, 123])) # False