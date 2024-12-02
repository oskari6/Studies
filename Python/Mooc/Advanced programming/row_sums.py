def row_sums(my_matrix: list):
    for row in my_matrix:
        sum = 0
        for item in row:
            sum += item
        row.append(sum)

if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)