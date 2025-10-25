input1 = int(input("Layers:"))
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
index = input1-1
dimensions = input1 + input1-1
figure = []
my_array = []
for _ in range(dimensions):
    figure.append([" "] * dimensions)

for layer in range(input1):
    char = letters[input1 - layer -1]
    for i in range(layer, dimensions - layer):
        for j in range(layer, dimensions - layer):
            figure[i][j] = char

for row in figure:
    for letter in row:
        print(letter, end="")
    print()