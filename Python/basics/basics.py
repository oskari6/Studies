import webbrowser
webbrowser.open("url")

#list in reverse
data = [1, 2, 3]
print(data[::-1])

def move_pos():
    pass
#unpacking data
data = [10, 20 ,30]
move_pos(*data)

#sets no duplicates
pets = []
print(list(set(pets)))

#all() check or any()
conditions = [

]
if all(conditions):
    pass

#joining
names = ["first name", "last name"]
full_name = " ".join(names)

#list comprehension
pets = ["animals"]
cleaned = [pet for pet in pets if pet not in["conditions"]]

#get index
for i, pet in enumerate(pets):
    print(pet, i)

#flatten list
pairs = []
flat = [item for pair in pairs for item in pair]

#comparing objects override same value
class Container():
    def __init(self, data):
        self.data = data

def __eq__(self, other):
    return self.data == other.data

Container.__eq__ = __eq__
x = Container(5)
y = Container(5)
print(x == y)

#iterator
import itertools

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, b + a

print(list(itertools.islice(fib(), 20)))

#zipping
from itertools import zip_longest
names = []
points = []
#without itertools zip(), wont get extra items
zipped = [list(item) for item in zip_longest(names, points)]
print(zipped)

#method default parameters
def zip_lists(list1=[], list2 = [], longest= True):
    if longest:
        pass
    else:
        pass
#notice order doesnt matter with default
print(zip_lists(longest=True, list2 =[], list1 = []))