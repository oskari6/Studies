def count_strings(n):
    if n == 1: return 26
    
    letters = [[0] * 26 for _ in range(n+1)] # to number values

    for c in range(26): letters[1][c] = 1

    for i in range(2, n +1):
        for c in range(26):
            if c - 1 >= 0:
                letters[i][c] += letters[i-1][c-1]
            if c + 1 < 26:
                letters[i][c] += letters[i-1][c+1]

    return sum(letters[n])

if __name__ == "__main__":
    print(count_strings(1)) # 26
    print(count_strings(2)) # 50
    print(count_strings(3)) # 98
    print(count_strings(4)) # 192

    print(count_strings(42)) # 36766943673096
    print(count_strings(100)) # 7073450400109633000218032957656