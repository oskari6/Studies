def count_numbers(a, b):
    def make_numbers(current):
        if current > b: return
        if a <= current <= b: valid_numbers.add(current)
        make_numbers(current * 10 +2)
        make_numbers(current * 10 +5)
    valid_numbers= set()
    make_numbers(0)
    return(len(valid_numbers))

if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512