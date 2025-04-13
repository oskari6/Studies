def find_first(size, steps):
    # Step 1: Build the base permutation
    perm = list(range(size))
    new_perm = perm[:]
    new_perm = new_perm[2:] + [1, 0]  # Apply one step

    def apply(p1, p2):
        return [p1[p2[i]] for i in range(size)]

    # Step 2: Fast exponentiation of the permutation
    result = list(range(size))
    power = steps
    current = new_perm[:]

    while power > 0:
        if power % 2 == 1:
            result = apply(current, result)
        current = apply(current, current)
        power //= 2

    # Step 3: result[i] tells where element i moved to.
    # We want to find i such that result[i] == 0
    for i in range(size):
        if result[i] == 0:
            return i + 1
if __name__ == "__main__":
    print(find_first(4, 3)) # 4
    print(find_first(12, 5)) # 11
    print(find_first(2, 1000)) # 1
    print(find_first(99, 555)) # 11
    print(find_first(12345, 10**6)) # 12295
    print(find_first(123456789, 1337**42)) # 111766959
