import re

def find_words(search_term):
    words = []

    if search_term.startswith("*"):
        pattern = re.compile(f".*{re.escape(search_term[1:])}$")
    elif search_term.endswith("*"):
        pattern = re.compile(f"{re.escape(search_term[:-1])}.*")
    else:
        pattern = re.compile(f"^{search_term.replace(".", ".")}$")

    with open("words.txt") as file:
        for word in file:
            word = word.strip()
            if pattern and pattern.match(word):
                words.append(word)
            elif search_term in word and not pattern:
                words.append(word)

    return words

if __name__ == "__main__":
    search_term = "reson*"
    print(find_words(search_term))