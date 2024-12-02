from random import randint

def roll(die):
    if die == "A":
        die = "333336"
    elif die == "B":
        die = "222555"
    elif die == "C":
        die = "144444"
    number = int(die[randint(0, len(die)-1)])
    return number

def play(die1, die2, times):
    die1_w = 0
    die2_w = 0
    ties = 0
    for i in range(times):
        total1 = 0
        total2 = 0
        if die1 == "A":
            die1 = "333336"
        elif die1 == "B":
            die1 = "222555"
        elif die1 == "C":
            die1 = "144444"
        total1 = die1[randint(0, len(die1)-1)]

        if die2 == "A":
            die2 = "333336"
        elif die2 == "B":
            die2 = "222555"
        elif die2 == "C":
            die2 = "144444"
        total2 = die2[randint(0, len(die2)-1)]

        if total1 > total2:
            die1_w += 1
        elif total2 > total1:
            die2_w += 1
        else:
            ties += 1

    return (die1_w, die2_w, ties)


if __name__ == "__main__":
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)