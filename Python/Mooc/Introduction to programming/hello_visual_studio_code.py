# Write your solution here
while True:
    guess = input("Editor: ")
    if guess.lower() == "word":
        print("awful")
    elif guess.lower() == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")