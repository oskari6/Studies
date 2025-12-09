# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"

class Room:
    def __init__(self):
        self.persons = []
    
    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        if self.persons:
            return False
        return True
    
    def print_contents(self):
        if self.persons:
            print(f"There are {len(self.persons)} persons in the room, and their combined height is {sum(person.height for person in self.persons)}")
            for person in self.persons:
                print(person)
        else:
            return None
        
    def shortest(self):
        if self.persons:
            shortest_person = min(self.persons, key=lambda person: person.height)
            return shortest_person
        else:
            return None
        
    def remove_shortest(self):
        if self.persons:
            removed = self.shortest()
            self.persons.remove(removed)
            return removed
        else:
            return None
if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()