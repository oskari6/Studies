# Write your solution here
my_list = [1, 2, 3, 4, 5]
while True:
    input1 = int(input("Index: "))
    if input1 < 0:
        break
    input2 = int(input("New value:"))

    my_list[input1] = input2
    print(my_list)
