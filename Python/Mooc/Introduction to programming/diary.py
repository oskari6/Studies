while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    task = int(input("Function: "))
    if task == 1:
        words = input("Diary entry:")
        with open("diary.txt", "a") as file:
            file.write(words+"\n")
        print("Diary saved")
    if task == 2:
        print("Entries:")
        with open("diary.txt") as file:
            for line in file:
                print(line)
    if task == 0:
        print("Bye now!")
        break