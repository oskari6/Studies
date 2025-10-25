# write your solution here
def matrix_sum():
    total = 0
    with open("matrix.txt") as file:
        for line in file:
            numbers = line.replace("\n", "").split(",")
            for num in numbers:
                total += int(num)
    return total

def matrix_max():
    max = 0
    with open("matrix.txt") as file:
        for line in file:
            numbers = line.replace("\n", "").split(",")
            for num in numbers:
                if int(num) > max:
                    max = int(num)
    return max

def row_sums():
    row_sums = []
    with open("matrix.txt") as file:
        for line in file:
            total = 0
            numbers = line.replace("\n", "").split(",")
            for num in numbers:
                total += int(num)
            row_sums.append(total)
    return row_sums

if __name__ == "__main__":
    sum = matrix_sum()
    print(sum)
    max = matrix_max()
    print(max)
    rows = row_sums()
    print(rows)
