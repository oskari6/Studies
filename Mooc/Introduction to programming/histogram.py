# Write your solution here
def histogram(word):
    letters = {}
    for letter in word:
        if letter not in letters:
            letters[letter] = "*"
        else:
            letters[letter] += "*"

    for letter,value in letters.items():
        print(letter,end=" ")
        print(value)

if __name__ == "__main__":
    histogram("abba")