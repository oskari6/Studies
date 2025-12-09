def count_substrings(string):
    seen = set()
    n = len(string)
    for i in range(n):
        for j in range(i,n):
            substring = string[i:j+1]
            seen.add(substring)
    return len(seen)
if __name__ == "__main__":
    print(count_substrings("aaaa")) # 4
    print(count_substrings("abab")) # 7
    print(count_substrings("abcd")) # 10
    print(count_substrings("abbbbbb")) # 13
    print(count_substrings("aybabtu")) # 26
    print(count_substrings("saippuakauppias")) # 110