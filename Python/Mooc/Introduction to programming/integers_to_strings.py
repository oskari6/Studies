# Write your solution here
def formatted(list:list):
    new = []
    for item in list:
        new.append(f"{item:.2f}")
    return new

if __name__ == "__main__":
    my_list = [1.00023, 0.987, 0.55543, 1.76]
    new_list = formatted(my_list)
    print(new_list)