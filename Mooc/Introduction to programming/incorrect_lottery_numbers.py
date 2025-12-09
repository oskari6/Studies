def filter_incorrect():
    correct = set()
    with open("lottery_numbers.csv") as file:
        for line in file:
            line = line.strip()
            new_line = line.split(";")
            weeks = new_line[0].split(" ")

            if len(weeks) != 2 or not weeks[1].isdigit():
                continue

            week_num = int(weeks[1])

            if not (1 <= week_num <= 52):
                continue

            numbers = new_line[1].split(",")
            if len(numbers) != 7:
                continue

            valid = True
            nums = set()

            for num in numbers:
                if not num.isdigit():
                    valid = False
                    break
                num_int = int(num)
                if not (1 <= num_int <= 39):
                    valid = False
                    break
                if num_int in nums:
                    valid = False
                    break
                nums.add(num_int)
            
            if valid:
                correct.add(line)
    
    with open("correct_numbers.csv", "w") as file:
        for line in sorted(correct):
            file.write(line+"\n")

if __name__ == "__main__":
    filter_incorrect()