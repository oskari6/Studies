# Write your solution here
def longest(strings: list):
    longest = ""
    for item in strings:
        if len(item) > len(longest):
            longest = item
    return longest
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))