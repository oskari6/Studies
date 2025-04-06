def count_numbers(length, numbers):
    numbers = sorted(numbers)
    total = 0

    if length > 1 and numbers == ["0"]: return 0    

    def backtrack(pos, last_index):
        if pos == length: return 1

        total = 0
        for i in range(last_index, len(numbers)):
            total += backtrack(pos + 1, i)
        return total

    for i in range(len(numbers)):
        if length > 1 and numbers[i] == "0":
            continue
        total += backtrack(1, i)

    return total if length > 1 else len(numbers)

if __name__ == "__main__":
    print(count_numbers(3, "123")) # 10
    print(count_numbers(5, "1")) # 1
    print(count_numbers(2, "137")) # 6
    print(count_numbers(8, "25689")) # 495
    print(count_numbers(1, "0")) # 1
    print(count_numbers(2, "0")) # 0
    print(count_numbers(10, "12")) # 11
    print(count_numbers(10, "123456789")) # 43758
    print(count_numbers(2, "01"))
    print(count_numbers(3, "001"))