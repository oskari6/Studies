class SimpleDate:
    def __init__(self,day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, another):
        return self.day == another.day and self.month == another.month and self.year == another.year
    
    def __ne__(self, another):
        return self.day != another.day or self.month != another.month or self.year != another.year
    
    def __lt__(self, another):
        if self.year < another.year:
            return True
        if self.year == another.year:
            if self.month < another.month:
                return True
            if self.month == another.month:
                if self.day < another.day:
                    return True
        return False
    
    def __gt__(self, another):
        if self.year > another.year:
            return True
        if self.year == another.year:
            if self.month > another.month:
                return True
            if self.month == another.month:
                if self.day > another.day:
                    return True
        return False
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
    
    def __add__(self, days):
        year = self.year 
        month = self.month
        day = self.day + days

        while day > 30:
            day -= 30
            month += 1
            if month > 12:
                month -= 12
                year += 1

        return SimpleDate(day, month, year)

    def __sub__(self, date):
        days1 = self.year * 360 + self.month * 30 + self.day
        days2 = date.year * 360 + date.month * 30 + date.day

        return abs(days1 - days2)
    
if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)