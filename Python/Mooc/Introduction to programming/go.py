# Write your solution here
def who_won(board: list):
    one = 0
    two = 0
    for row in board:
        for spot in row:
            if spot == 1:
                one += 1
            elif spot == 2:
                two += 1
            else:
                continue
    return 1 if one > two else 2 if two > one else 0

if __name__ == "__main__":
    array = [[1, 2, 2, 2], [2, 1, 1, 1], [0, 2, 1, 0]]
    result = who_won(array)
    print(result)