# write your solution here
def read_fruits():
    fruits = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            fruit = line.split(";")
            fruits[fruit[0]] = float(fruit[1])
    new_file.close()
    return fruits

if __name__ == "__main__":
    fruits = read_fruits()
    print(fruits)