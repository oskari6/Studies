def find_number(numbers):
    if numbers[0] != numbers[1] and numbers[0] != numbers[2]:
        return numbers[0]
    for i in range(len(numbers)):
        current = numbers[i]
        if current != numbers[i+1]: return numbers[i+1]

if __name__ == "__main__":
    print(find_number([1, 1, 1, 2])) # 2
    print(find_number([1, 1, 2, 1])) # 2
    print(find_number([1, 2, 1, 1])) # 2
    print(find_number([2, 1, 1, 1])) # 2
    print(find_number([5, 5, 5, 3, 5])) # 3
    print(find_number([1, 100, 1])) # 100
    print(find_number([2, 2, 9, 2, 2, 2, 2, 2])) # 100

    numbers = [1] * 10**5 + [2]
    print(find_number(numbers)) # 2