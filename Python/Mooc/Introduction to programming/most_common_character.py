# Write your solution here
def most_common_character(word):
    high = ""
    most = 0
    for c in word:
        count = word.count(c)
        if count > most:
            most = count
            high = c
    return high

if __name__ == "__main__":
    word = "abcdbde"
    print(most_common_character(word))