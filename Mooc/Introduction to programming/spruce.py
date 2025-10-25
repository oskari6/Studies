# Write your solution here
def spruce(size):
    print("a spruce!")
    spruce = "*"
    width = (size * 2) -1

    for i in range(size, 0, -1):
        print(spruce.center(width))
        spruce += "**"
    print("*".center(width))

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)