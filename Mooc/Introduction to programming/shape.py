# Copy here code of line function from previous exercise and use it in your solution
def line(size, x):
    if x == "":
        print("*" * size)
    else:
        print(x[0] * size)

def shape(triangle, char1, height, char2):
    for i in range(triangle+1):
        line(i, char1)
    for j in range(height):
        line(i, char2)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")