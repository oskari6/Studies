# Write your solution here
my_list = []
count = 1
while True:
    print(f"The list is now {my_list}")
    input1 = input("a(d)d, (r)emove or e(x)it:")
    if input1 == "d":
        my_list.append(count)
        count += 1
    if input1 == "r":
        my_list.pop()
        count -= 1
    if input1 == "x":
        print("Bye!")
        break
