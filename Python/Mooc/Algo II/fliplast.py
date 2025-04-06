def find_first(size, steps):
    def f(i):
        if i >= 2:
            return i - 2
        elif i == 0:
            return size - 1
        elif i == 1:
            return size - 2

    def fast_pow_f(i, power):
        # Jump index through f function power times using binary exponentiation
        memo = {}

        # Precompute f^1, f^2, f^4, ..., f^(2^k)
        curr = {}
        for j in range(size):
            curr[j] = f(j)
        memo[1] = curr

        max_pow = 1
        while max_pow * 2 <= power:
            prev = memo[max_pow]
            new_map = {}
            for j in range(size):
                new_map[j] = prev[prev[j]]
            max_pow *= 2
            memo[max_pow] = new_map

        # Apply exponentiation
        result = 0
        for exp in sorted(memo.keys(), reverse=True):
            if power >= exp:
                result = memo[exp][result]
                power -= exp
        return result

    final_index = fast_pow_f(0, steps)
    return final_index + 1

if __name__ == "__main__":
    print(find_first(4, 3)) # 4
    print(find_first(12, 5)) # 11
    print(find_first(2, 1000)) # 1
    print(find_first(99, 555)) # 11
    print(find_first(12345, 10**6)) # 12295
    print(find_first(123456789, 1337**42)) # 111766959
