def find_sequence(numbers):
    length = len(numbers)
    result = [[] for _ in range(length)]

    for i in range(length):
        result[i] = [numbers[i]]
        for j in range(i):
            if numbers[j] < numbers[i] and len(result[j]) + 1 > len(result[i]):
                result[i] = result[j] + [numbers[i]]
            elif numbers[j] < numbers[i] and len(result[j]) + 1 == len(result[i]):
                new = result[j] + [numbers[i]]
                if new < result[i]:
                    result[i] = new
    # right order
    return max(result, key=lambda seq: (len(seq), [-x for x in seq])) if result else []

if __name__ == "__main__":
    print(find_sequence([1, 2, 3])) # [1, 2, 3]
    print(find_sequence([3, 2, 1])) # [1]
    print(find_sequence([1, 1, 1, 1, 1])) # [1]

    print(find_sequence([1, 8, 2, 7, 3, 6])) # [1, 2, 3, 6]
    print(find_sequence([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    print(find_sequence([4, 1, 5, 6, 3, 4, 3, 8])) # [1, 3, 4, 8]