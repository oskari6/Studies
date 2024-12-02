# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    total = 0

    for i in range(len(my_matrix)):
        for j in range(len(my_matrix[i])):
            if my_matrix[i][j] == element:
                total += 1
    return total
if __name__ == "__main__":
    m = [[1, 2, 3], [2, 3, 1], [4, 5, 6]]
    print(count_matching_elements(m, 2))