def find_rounds(numbers):
    current = 1
    count = 0
    new_list = []
    temp = []
    while count != len(numbers):
        for i in range(0, (len(numbers))):
            if numbers[i] == current:
                temp.append(current)
                current += 1 
                count += 1
        new_list.append(temp)
        temp = []
    return new_list      

if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]