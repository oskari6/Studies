def most_common_words(filename, lower_limit):
    with open(filename) as file:
        words = [word.strip(".,") for line in file for word in line.split()]
        counts = {word: 0 for word in set(words)}
        for word in words:
            counts[word] += 1
        counts = {word:count for word,count in counts.items() if count >= lower_limit}
        print(counts)
        return counts

if __name__ == "__main__":
    most_common_words("comprehensions.txt", 3)