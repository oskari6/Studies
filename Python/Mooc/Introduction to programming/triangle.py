# Copy here code of line function from previous exercise
def line(size, x):
    if x == "":
        print("*" * size)
    else:
        print(x[0] * size)

def triangle(size):
    # You should call function line here with proper parameters
    for i in range(size+1):
        line(i, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
