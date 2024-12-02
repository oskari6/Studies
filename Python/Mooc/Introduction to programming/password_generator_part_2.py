from random import randint
from random import shuffle

def generate_strong_password(length, numbers, specials):
    letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "1234567890"
    special_chars = "!?=+-()#"

    in_use = letters
    if numbers:
        in_use += digits
    if specials:
        in_use += special_chars

    password = ""
    
    password += letters[randint(0, len(letters)-1)]
    length -= 1
    
    if numbers:
        password += digits[randint(0, len(digits) -1)]
        length -=1
    if specials:
        password += special_chars[randint(0, len(special_chars) -1)]
        length -=1
        
    for i in range(length):
        rand_num = randint(0, len(in_use)-1)
        password += in_use[rand_num]
    
    password = list(password)
    shuffle(password)
    password = ''.join(password)
    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))