# write your solution here
def largest():
    nums = []
    with open("numbers.txt") as new_file:
        for line in new_file:
            nums.append(line)
    new_file.close()
    return int(max(nums))

if __name__ == "__main__":
    big = largest()
    print(big)