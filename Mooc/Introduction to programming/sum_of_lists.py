# Write your solution here
def list_sum(list1:list, list2 : list) -> list:
    new = []
    for i in range(len(list1)):
        sum = list1[i] + list2[i]
        new.append(sum)
    return new

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    new = list_sum(a, b)
    print(new)