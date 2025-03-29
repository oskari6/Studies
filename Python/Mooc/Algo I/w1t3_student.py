import math


def check_number(number):
    sum = 0
    if number[0] != "0" or len(number) != 9:
        return False
    
    multiples = [3,7,1,3,7,1,3,7]
    for i in range(len(number)-1):
        sum += (multiples[i] * int(number[i]))
    return number[-1] == str((math.ceil(sum/10)*10 - sum))

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False