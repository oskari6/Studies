import difflib

input1 = input("write text:")
text = input1.split()
new = set()
wrong = []

with open("wordlist.txt") as file:
    for line in file:
        new.add(line.strip())

for i in range(len(text)):
    if text[i] not in new and i != 0:
        wrong.append(text[i])
        text[i] = "*" + text[i] + "*"   

corrected = " ".join(text)
print(corrected)

for word in wrong:
    wrong_word = word
    matches = difflib.get_close_matches(wrong_word, new)
    print("suggestions:")
    print(f"{wrong_word}: ", end="")
    if matches:
        print(", ".join(matches))
