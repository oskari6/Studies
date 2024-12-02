def new_person(name, age):
    combined = (name, age)
    names = name.split()
    print(len(names))
    if name == "" or len(names) < 2 or len(name) > 40 or age < 0 or age > 150:
        raise ValueError("Value error")
    else:
        return combined

if __name__ == "__main__":
    new_person("Andrew", 23)