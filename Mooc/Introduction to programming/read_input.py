def read_input(msg, num1, num2):
    while True:
        try:
            num = int(input(msg))
            if num < num1 or num > num2:
                raise ValueError(f"You must type in an integer between {num1} and {num2}")
            else:
                return num
        except ValueError:
            print((f"You must type in an integer between {num1} and {num2}"))

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)