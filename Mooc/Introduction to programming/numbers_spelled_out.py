def dict_of_numbers():
    new = {}
    to_ten = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    tens = {10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
    teens = {11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
    for i in range(0, 100):
        if i < 10:
            new[i] = to_ten[i]
        elif i >= 11 and i < 20:
            new[i] = teens[i]
        elif i % 10 == 0:
            new[i] = tens[i]
        else:
            part1 = i // 10 * 10
            part2 = i % 10
            new[i] = f"{tens[part1]}-{to_ten[part2]}"

    return new

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])