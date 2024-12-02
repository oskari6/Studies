input1 = input("Write text:")
text = input1.split()
new = set()

with open("wordlist.txt") as file:
    for line in file:
        new.add(line.strip())

for i in range(len(text)):
    if text[i] not in new and i != 0:
        text[i] = "*" + text[i] + "*"         

corrected = " ".join(text)

print(corrected)
