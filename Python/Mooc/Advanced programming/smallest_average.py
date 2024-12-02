def smallest_average(person1: dict, person2: dict, person3: dict):
    persons = [
        (person1, (person1["result1"] + person1["result2"] + person1["result3"]) / 3),
        (person2, (person2["result1"] + person2["result2"] + person2["result3"]) / 3),
        (person3, (person3["result1"] + person3["result2"] + person3["result3"]) / 3)
    ]

    smallest = min(persons, key=lambda x: x[1])[0]

    return smallest

if __name__ == "__main__":
    person1 = {"name": "Anna", "result1": 3,"result2": 3,"result3": 3}
    person2 = {"name": "Gary", "result1": 5,"result2": 5,"result3": 5}
    person3 = {"name": "Larry", "result1": 1,"result2": 1,"result3": 1}

    print(smallest_average(person1, person2, person3))