
# Write your solution here
def longest_series_of_neighbours(nums):
    count = 1
    high = 1
    for num in range(1, len(nums)):
        if abs(nums[num] - nums[num-1]) == 1:
            count += 1
        else:
            count = 1
        if count > high:
            high = count
    return high

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))