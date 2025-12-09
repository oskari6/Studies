def create_distribution(string):
    lengths = {}
    n = len(string)
    seen = set()

    for i in range(n):
        for j in range(i,n):
            substring = string[i:j+1]
            if substring not in seen:
                seen.add(substring)
                substring_length = len(substring)
                if substring_length in lengths: lengths[substring_length] += 1
                else: lengths[substring_length] = 1

    return lengths

if __name__ == "__main__":
    print(create_distribution("aaaa"))
    # {1: 1, 2: 1, 3: 1, 4: 1}
    
    print(create_distribution("abab"))
    # {1: 2, 2: 2, 3: 2, 4: 1}
    
    print(create_distribution("abcd"))
    # {1: 4, 2: 3, 3: 2, 4: 1}

    print(create_distribution("abbbbbb"))
    # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 1}

    print(create_distribution("aybabtu"))
    # {1: 5, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}