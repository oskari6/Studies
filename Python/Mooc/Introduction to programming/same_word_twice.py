# Write your solution here
my_list = []
count = 0
while True:
    input1 = input("Word:")
    if input1 in my_list:
        print(f"You typed in {count} different words")
        break
    else:
        my_list.append(input1)
        count += 1