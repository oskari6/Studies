import re

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    input1 = int(input("Function:"))
    if input1 == 1:
        word = input("The word in Finnish:")
        word2 = input("The word in English:")
        with open("dictionary.txt", "a") as file:
            file.write(f"{word};{word2}\n")
        print("Dictionary entry added")
    if input1 == 2:
        search_term = input("Search term:")
        pattern = re.compile(f".*{re.escape(search_term)}.*")

        with open("dictionary.txt") as file:
            for word in file:
                words = word.strip().split(";")
                if pattern.match(words[0]) or pattern.match(words[1]):
                    print(f"{words[0]} - {words[1]}")
    if input1 == 3:
        print("Bye!")
        break