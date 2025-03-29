def find_segments(data):
    temp = []
    current = data[0]
    count = 0
    for i in range(len(data)):
        if data[i] != current:
            temp.append((count, current))
            current = data[i]
            count = 0
        count += 1
    temp.append((count, current))
    return temp

if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]