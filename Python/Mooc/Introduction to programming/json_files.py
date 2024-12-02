import json

def print_persons(filename):
    with open(filename) as file:
        data = file.read()

    persons = json.loads(data)
    for person in persons:
        name = person["name"]
        age = person["age"]
        hobbies = person["hobbies"]

        hobbies = ", ".join(hobbies)

        print(f"{name} {age} years (", end="")
        print(f"{hobbies}",end=")")
        print()

if __name__ == "__main__":
    print_persons("file1.json")