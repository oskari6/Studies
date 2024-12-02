# Write your solution here
def everything_reversed(list:list):
    new = []
    for item in list:
        new.append(item[::-1])
    return new[::-1]

if __name__ == "__main__":
    my_list = ["1", "2", "3", "4"]
    new_list = everything_reversed(my_list)
    print(new_list)