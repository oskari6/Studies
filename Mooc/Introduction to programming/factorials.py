# Write your solution here
def factorials(n: int):
    nums = {}
    for num in range(1, n+1):
        key = num
        factorial  = 1
        for val in range(1, num+1):
            factorial *= val
        nums[key] = factorial

    return nums

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])