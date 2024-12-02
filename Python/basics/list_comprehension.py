import math

#exponent
data = [1, 2, 3, 4]
new_data = []

new_data = [math.sqrt(d) for d in data]
print(new_data)

#reverse list
names = ['name1', 'name2', 'name3']
reversed = [name[::-1] for name in names]

#even
data = [1, 34, 35, 65, 23, 3, 3, 72, 65, 34, 45,78, 98, 23, 15, 16, 17, 18, 10]

new_data = []
new_data = [d for d in data if d % 2 == 0]

#nested
scores = [[1, 2, 3], [2, 3, 4], [9, 3, 4]]
scores_new = [score for scores in scores for score in scores]

#else on the left, ternary operator
tiers = ['gold', 'gold', 'bronze', 'silver', 'free', None, None, 'free', 'bronze', 'silver', None]
cleaned = ['free' if tier is None else tier for tier in tiers]

#get possible combinations
letters = ['c', 's', 'v']
collection = [[first, second, third] for first in letters for second in letters for third in letters]
print(len(collection))

#dictionary
titles = ["one", "two", "three"]
codes = {letter:title for letter, title in zip(letters, titles)}
#without conditions, upper can have ifs
simple = dict(zip(letters, titles))

print(codes)
print(simple)

#flip key and value, unique key can be a problem
flipped = {value:key for key, value in codes.items()}
print(flipped)

#tuples
tuple = [("one", 123), ("two", 2), ("three", 3)]
flipped = [(user[1], user[0]) for user in tuple]
print(flipped)