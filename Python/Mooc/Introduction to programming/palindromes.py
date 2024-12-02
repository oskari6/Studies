# Note, that at this time the main program should not be written inside

# Write your solution here
# Write your solution here
def palindromes(word):
    temp = word[::-1]
    if word == temp:
        return True
    else:
        return False
    
while True:
    input1 = input("Please type in a palindrome:")
    if palindromes(input1):
        print(f"{input1} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")