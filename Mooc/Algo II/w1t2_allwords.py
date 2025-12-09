import itertools

def create_words(word):
    words = set()
    for entry in itertools.permutations(word):
        valid = test_valid(entry)
        if valid: words.add("".join(entry))

    return sorted([word for word in words])

def test_valid(word):
    for i in range(len(word)-1):
        if word[i+1] == word[i]:
            return False
        
    return True

if __name__ == "__main__":
    print(create_words("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create_words("aab")) # ['aba']
    print(create_words("aaab")) # []

    print(create_words("kala"))
    # ['akal', 'akla', 'alak', 'alka', 'kala', 'laka']

    print(create_words("syksy"))
    # ['ksysy', 'kysys', 'skysy', 'syksy', 'sykys', 'sysky', 
    #  'sysyk', 'yksys', 'ysksy', 'yskys', 'ysyks', 'ysysk']

    print(len(create_words("aybabtu"))) # 660
    print(len(create_words("abcdefgh"))) # 40320
    print(create_words("ba"))