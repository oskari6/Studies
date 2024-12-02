# Write your solution here
def shortest(list:list):
    short = list[0]
    for word in list:
        if len(word) < len(short):
            short = word
    
    return short

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    short = shortest(my_list)
    print(short)