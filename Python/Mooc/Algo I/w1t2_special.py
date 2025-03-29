import math


def check_year(year):
    year = str(year)
    return math.pow((int(year[:2])+int(year[2:])),2) == int(year)

if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False