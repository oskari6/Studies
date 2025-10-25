# Write your solution here
def length_of_longest(list:list):
    longest = list[0]
    for word in list:
        if len(word) > len(longest):
            longest = word
    
    return len(longest)

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    long = length_of_longest(my_list)
    print(long)