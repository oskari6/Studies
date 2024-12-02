# Write your solution here!
class  NumberStats:
    
    def __init__(self):
        self.num_list = []
        self.numbers = 0

    def add_number(self, number:int):
        self.num_list.append(number)
        self.numbers += 1

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        if self.numbers:
            return sum(self.num_list) if self.numbers else 0

    def average(self):
        if self.numbers:
            return sum(self.num_list) / len(self.num_list) if self.numbers else 0

def input_numbers(even_stats, odd_stats, both_stats):
    print("Please type in integer numbers:")
    while True:
        num = int(input())
        if num == -1:
            break
        if num % 2 == 0:
            even_stats.add_number(num)
        else:
            odd_stats.add_number(num)
        both_stats.add_number(num)

# Define instances
even = NumberStats()
odd = NumberStats()
both = NumberStats()

# Run the program
input_numbers(even, odd, both)

# Print the required outputs
print(f"Sum of numbers: {both.get_sum()}")
print(f"Mean of numbers: {both.average()}")
print(f"Sum of even numbers: {even.get_sum()}")
print(f"Sum of odd numbers: {odd.get_sum()}")
