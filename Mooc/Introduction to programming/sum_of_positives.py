# Write your solution here
def sum_of_positives(list:list):
    sum = 0
    for num in list:
        if num > 0:
            sum += num
    return sum

if __name__ == "__main__":
    sum = sum_of_positives([1, -2, 3, -4, 5])
    print(sum)