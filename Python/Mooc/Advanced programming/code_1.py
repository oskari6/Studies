class Item:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.name()} ({self.weight()} kg)"


class Suitcase:
    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.__items = []
        
    def add_item(self, item):
        if self.weight() + item.weight() <= self.__max_weight:
            self.__items.append(item)

    def print_items(self):
        for item in self.__items:
            print(f"{item.name()} ({item.weight()} kg)")

    def weight(self):
        return sum(item.weight() for item in self.__items)
    
    def __str__(self):
        items_weight = self.weight()
        if len(self.__items) != 1:
            return f"{len(self.__items)} items ({items_weight} kg)"
        else:
            return f"{len(self.__items)} item ({items_weight} kg)"

    def heaviest_item(self):
        if len(self.__items) == 0:
            return None
        else:
            return max(self.__items, key=lambda item: item.weight())
        
class CargoHold:
    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.__cargo = []

    def add_suitcase(self, suitcase):
        if self.weight() + suitcase.weight() <= self.__max_weight:
            self.__cargo.append(suitcase)

    def print_items(self):
        for suitcase in self.__cargo:
            suitcase.print_items()

    def weight(self):
        return sum(suitcase.weight() for suitcase in self.__cargo)
    
    def __str__(self):
        if len(self.__cargo) == 1:
            return f"{len(self.__cargo)} suitcase, space for {self.__max_weight - self.weight()} kg"
        return f"{len(self.__cargo)} suitcases, space for {self.__max_weight - self.weight()} kg"

if __name__ == "__main__":
    suitcase = Suitcase(25)
    item = Item("ABC Book", 2)
    suitcase.add_item(item)
    heaviest = suitcase.heaviest_item()
    print(heaviest.name())