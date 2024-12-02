# Write your solution here
input1 = int(input("Please type in a positive integer: "))

for i in range(-input1, input1+1):
    if i == 0:
        continue
    print(i)