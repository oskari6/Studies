from random import randint
def generate_password(length):
    letters = "abcdefghijklmnopqrstuvwxyz"
    password = ""
    for i in range(length):
        rand_num = randint(0, len(letters)-1)
        password += letters[rand_num]

    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))