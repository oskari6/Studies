def first_wins(numbers):
    n = len(numbers)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i+1] = prefix_sums[i] + numbers[i]

    max_score = [[0] * n for _ in range(n)]

    for length in range(1, n+1):
        for i in range(n - length + 1):
            j = i + length -1
            total = prefix_sums[j +1] - prefix_sums[i]
            if i == j:
                max_score[i][j] = numbers[i]
            else:
                max_score[i][j] = max(
                    numbers[i] + (total-numbers[i]-max_score[i+1][j]),
                    numbers[j] + (total-numbers[j]-max_score[i][j-1])
                )

    player1 = max_score[0][n-1]
    total_sum = prefix_sums[n]
    player2 = total_sum-player1
    return player1 > player2

    

if __name__ == "__main__":
    print(first_wins([2, 1, 3])) # True
    print(first_wins([1, 3, 1])) # False

    print(first_wins([1])) # True
    print(first_wins([1, 1])) # False
    print(first_wins([1, 5])) # True
    print(first_wins([1, 1, 1])) # True
    print(first_wins([1, 2, 3, 4])) # True
    print(first_wins([1, 3, 3, 7, 4, 2, 1])) # False

    print(first_wins([1] * 50)) # False
    print(first_wins([1, 2] * 25)) # True