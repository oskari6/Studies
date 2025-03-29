def count_pairs(numbers):
    if len(numbers) < 1: return 0
    numbers = sorted(numbers)
    small = 0
    large = len(numbers)//2
    count = 0
    while small < len(numbers) // 2 and large < len(numbers):
        if numbers[small] * 2 <= numbers[large]:
            count += 1
            small += 1
        large += 1

    return count 

if __name__ == "__main__":
    print(count_pairs([1])) # 0
    print(count_pairs([1, 2, 3])) # 1
    print(count_pairs([1, 2, 3, 4])) # 2
    print(count_pairs([1, 1, 1, 1])) # 0
    print(count_pairs([10**9, 1, 1, 1])) # 1
    print(count_pairs([4, 5, 1, 4, 7, 8])) # 2
    print(count_pairs([1, 2, 3, 2, 4, 6])) # 3

    numbers = [(x * 999983) % 10**6 + 1 for x in range(10**5)]
    print(count_pairs(numbers)) # 41176