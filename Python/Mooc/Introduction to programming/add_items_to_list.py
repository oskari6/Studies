# Write your solution here
num = int(input("How many items: "))
my_list = []
for i in range(num):
    item = int(input(f"Item {i+1}:"))
    my_list.append(item)
print(my_list)