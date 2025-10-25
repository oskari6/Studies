contacts = {}
while True:
    num = int(input("command (1 search, 2 add, 3 quit):"))
    if num == 1:
        name = input("name:")
        if name not in contacts:
            print("no number")
            continue
        print(contacts[name])

    if num == 2:
        name = input("name:")
        number = input("number:")
        contacts[name] = number
        print("ok!")
    if num == 3:
        print("quitting...")
        break