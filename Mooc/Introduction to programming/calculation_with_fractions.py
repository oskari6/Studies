from fractions import Fraction

def fractionate(amount):
    fraction = Fraction(1)

    part = fraction / amount
    parts = [part] * amount

    return parts

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))