from random import randint

def word_generator(characters, length, amount):
    times = 0
    while times < amount:
        word = ""
        for i in range(length):
            rand_num = randint(0, len(characters)-1)
            word += characters[rand_num]
        yield word
        times += 1


if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)