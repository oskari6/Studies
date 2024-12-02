# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents
    
    def __ne__(self, another):
        return self.__euros != another.__euros or self.__cents != another.__cents
    
    def __gt__(self, another):
        if self.__euros > another.__euros or (self.__euros == another.__euros and self.__cents > another.__cents):
            return True
        return False
    
    def __lt__(self, another):
        if self.__euros < another.__euros or (self.__euros == another.__euros and self.__cents < another.__cents):
            return True
        return False

    def __add__(self, another):
        total_euros = self.__euros + another.__euros
        total_cents = self.__cents + another.__cents
        
        if total_cents >= 100:
            extra = total_cents // 100
            total_cents = total_cents % 100
            total_euros += extra

        return Money(total_euros, total_cents)
    
    def __sub__(self, another):
        total_cents = self.__euros * 100 + self.__cents - (another.__euros * 100 + another.__cents)

        if total_cents < 0:
            raise ValueError(f"a negative result is not allowed")
        
        euros = total_cents // 100
        cents = total_cents % 100

        return Money(euros, cents)
    

if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1