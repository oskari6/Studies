from random import sample

def words(n, beginning):
    words = []
    with open("words.txt") as file:
        for word in file:
            word = word.strip()
            if word.startswith(beginning):
                words.append(word)

    if len(words) < n:
        raise ValueError()
    
    selected = sample(words, n)

    return selected

if __name__ == "__main__":
    word_list = words(2, "car")
    print(len(word_list))
    for word in word_list:
        print(word)