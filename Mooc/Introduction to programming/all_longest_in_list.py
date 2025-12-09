# Write your solution here
def all_the_longest(list:list):
    longest = []
    max_long = 0

    for word in list:
        if len(word) > max_long:
            max_long = len(word)
            longest = [word]
        elif len(word) == max_long:
            longest.append(word)

    return longest

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    longest = all_the_longest(my_list)
    print(longest)