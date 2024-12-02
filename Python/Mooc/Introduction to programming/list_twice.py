# Write your solution here
my_list = []
while True:
    input1 = int(input("New Item:"))
    if input1 == 0:
        print("Bye!")
        break
    my_list.append(input1)
    print(f"The list now: {my_list}")
    print(f"The list in order: {sorted(my_list)}")
    