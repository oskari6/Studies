import math

class LunchCard:
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"
    
    def eat_lunch(self):
        if (self.balance - 2.6) < 0:
            return
        self.balance -= 2.6
    
    def eat_special(self):
        if (self.balance - 4.6) < 0:
            return
        self.balance -= 4.6

    def deposit_money(self, amount):
        if amount < 0:
            raise ValueError("ValueError: You cannot deposit an amount of money less than zero")
        self.balance += amount

peter = LunchCard(20)
grace = LunchCard(30)
peter.eat_special()
grace.eat_lunch()
print("Peter:", peter)
print("Grace:", grace)
peter.deposit_money(20)
grace.eat_special()
print("Peter:", peter)
print("Grace:", grace)
peter.eat_lunch()
peter.eat_lunch()
grace.deposit_money(50)
print("Peter:", peter)
print("Grace:", grace)
    