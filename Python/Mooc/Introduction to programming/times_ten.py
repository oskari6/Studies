# Write your solution here
def times_ten(start_index: int, end_index : int):
    nums = {}
    for num in range(start_index, end_index+1):
        nums[num] = num*10

    return nums

if __name__ == "__main__":
    nums = times_ten(3, 6)
    print(nums)