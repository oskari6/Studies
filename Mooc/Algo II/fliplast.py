def find_first(size, steps):
    # Create the initial permutation
    P = list(range(size))
    # Move first two elements to end in reverse order
    P = P[2:] + [1, 0]  # Only affects indices

    # Function to compose two permutations
    def compose(A, B):
        return [B[a] for a in A]

    # Exponentiation by squaring of the permutation
    def permute_pow(P, power):
        result = list(range(size))  # Identity permutation
        while power > 0:
            if power % 2 == 1:
                result = compose(result, P)
            P = compose(P, P)
            power //= 2
        return result

    final_perm = permute_pow(P, steps)
    return final_perm[0] + 1

if __name__ == "__main__":
    print(find_first(4, 3)) # 4
    print(find_first(12, 5)) # 11
    print(find_first(2, 1000)) # 1
    print(find_first(99, 555)) # 11
    print(find_first(12345, 10**6)) # 12295
    print(find_first(123456789, 1337**42)) # 111766959