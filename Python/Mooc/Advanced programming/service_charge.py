class BankAccount:
    def __init__(self, name, num, balance):
        self.__name = name
        self.__num = num
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        tax = self.__balance * 0.01
        self.__service_charge(tax)

    def withdraw(self, amount):
        self.__balance -= amount
        tax = self.__balance * 0.01
        self.__service_charge(tax)

    def __service_charge(self, tax):
        self.__balance -= tax
    
    @property
    def balance(self):
        return self.__balance
    
if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)