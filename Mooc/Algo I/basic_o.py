# O(1)
def middle(numbers):
    n = len(numbers)
    return numbers[n // 2]

# O(n)
def calc_sum(numbers):
    result = 0
    for x in numbers:
        result += x
    return result

# 0(n^2)
def has_sum(numbers, x):
    for a in numbers:
        for b in numbers:
            if a + b == x:
                return True
    return False

# Sequential code segments O(n) here
def count_min(numbers):
    # stage 1
    min_value = numbers[0]
    for x in numbers:
        if x < min_value:
            min_value = x

    # stage 2
    result = 0
    for x in numbers:
        if x == min_value:
            result += 1

    return result