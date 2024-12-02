# Write your solution here
def even_numbers(list:list) -> list:
    even = []
    for num in list:
        if num % 2 == 0:
            even.append(num)
    return even

if __name__ == "__main__":
    original = [1, 2, 3, 4, 5]
    even = even_numbers(original)
    print("original ", original)
    print("new", even)