# Write your solution here
# Write your solution here
def no_shouting(list:list):
    new = []
    for word in list:
        if not word.isupper():
            new.append(word)
    return new

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    new = no_shouting(my_list)
    print(new)