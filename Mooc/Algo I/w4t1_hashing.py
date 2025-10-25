def hash_value(string):
    a = 23
    m = 2**32
    values = {}
    total = 0
    n = len(string)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i, char in enumerate(alphabet): values[char] = i
    for i in range(n):
        char_value = values[string[i]]
        total = (total + char_value * pow(a, n-1-i, m)) % m
    return total

if __name__ == "__main__":
    print(hash_value("abc")) # 25
    print(hash_value("kissa")) # 2905682
    print(hash_value("aybabtu")) # 154753059
    print(hash_value("tira")) # 235796
    print(hash_value("zzzzzzzzzz")) # 2739360440