def prime_numbers():
    num = 2
    while True:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))