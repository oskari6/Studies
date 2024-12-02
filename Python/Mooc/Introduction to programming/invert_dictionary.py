# Write your solution here
def invert(dictionary: dict):
    new = {}
    for key, value in dictionary.items():
        new[value] = key
    dictionary.clear()
    dictionary.update(new)

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)