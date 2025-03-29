def count_rounds(numbers):
    temp = set()
    count = 0
    maximum = max(numbers)
    for i,num in enumerate(numbers):
        if num == maximum: count += 1
        elif num+1 in temp: count += 1
        temp.add(num)
    return count

if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([4, 1, 3, 2])) # 3
    print(count_rounds([1])) # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4
    print(count_rounds([3, 1, 2])) # 2
    print(count_rounds([2, 1, 3])) # 2
    print(count_rounds([2, 5, 4, 1, 3])) # 4
    print(count_rounds([2, 5, 3, 1, 4])) # 3

    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000
