def count_splits(sequence):
    total_zeros = sequence.count("0")
    total_ones = sequence.count("1")

    first_zeros = 0
    first_ones = 0
    valid = 0

    for i in range(len(sequence) - 1):
        if sequence[i] == "0": first_zeros += 1
        else: first_ones += 1

        second_zeros = total_zeros - first_zeros
        second_ones = total_ones - first_ones

        if first_zeros == first_ones and second_zeros == second_ones:
            valid += 1

    return valid


if __name__ == "__main__":
    print(count_splits("00")) # 0
    print(count_splits("01")) # 0
    print(count_splits("0110")) # 1
    print(count_splits("010101")) # 2
    print(count_splits("000111")) # 0
    print(count_splits("01100110")) # 3
    print(count_splits("1011111010")) # 0

    sequence = "01"*10**5
    print(count_splits(sequence)) # 99999
