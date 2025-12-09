# Write your solution here
def distinct_numbers(list:list) -> list:
    new = []
    for num in list:
        if num in new:
            continue
        new.append(num)
    
    return sorted(new)

if __name__ == "__main__":
    my_list = [5, 6, 7, 8, 8, 9, 9, 5]
    new = distinct_numbers(my_list)
    print(new)