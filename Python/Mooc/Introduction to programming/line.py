# Write your solution here
def line(size, x):
    if x == "":
        print("*" * size)
    else:
        print(x[0] * size)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "XXX")