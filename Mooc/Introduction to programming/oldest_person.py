def oldest_person(people: list):
    oldest = 0
    name_oldest = ""
    for person in people:
        name, birth = person
        age = 2024 - birth
        if age > oldest:
            oldest = age
            name_oldest = name
    return name_oldest

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]
    oldest = oldest_person(people)
    print(oldest)