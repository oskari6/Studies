def filter_forbidden(string, forbidden):
    return "".join([letter for letter in string if letter not in forbidden])

if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)