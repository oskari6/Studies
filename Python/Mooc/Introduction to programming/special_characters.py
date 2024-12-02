import string

def separate_characters(my_string):
    ascii = string.ascii_letters
    punctuation = string.punctuation

    first = ''.join([char for char in my_string if char in ascii])
    second = ''.join([char for char in my_string if char in punctuation])
    third = ''.join([char for char in my_string if char not in ascii and char not in punctuation])
    strings = (first, second, third)
    return strings

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])