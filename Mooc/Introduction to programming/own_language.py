import string
def run(program):
    prints = []
    locations = {}
    vars = {
        "A": 0, "B": 0, "C": 0, "D": 0, "E": 0,
        "F": 0, "G": 0, "H": 0, "I": 0, "J": 0,
        "K": 0, "L": 0, "M": 0, "N": 0, "O": 0,
        "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0,
        "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0,
        "Z": 0
    }
    
    for index, line in enumerate(program):
        if line.endswith(":"):
            label = line[:-1]
            locations[label] = index

    index = 0
    while index < len(program):
        line = program[index]

        if line.startswith("PRINT"):
            parts = line.split()
            if parts[1] in vars:
                prints.append(vars[parts[1]])
            else:
                prints.append(int(parts[1]))

        elif line.startswith("MOV"):
            parts = line.split()
            if parts[2] in vars:
                vars[parts[1]] = vars[parts[2]]
            else:
                vars[parts[1]] = int(parts[2])
        elif line.startswith("ADD"):
            parts = line.split()
            key = parts[1]
            value = parts[2]
            if value in vars:  # Check if 'value' is a variable name
                vars[key] += vars[value]
            else:
                vars[key] += int(value)
        elif line.startswith("SUB"):
            parts = line.split()
            key = parts[1]
            value = parts[2]
            if value in vars:  # Check if 'value' is a variable name
                vars[key] -= vars[value]
            else:
                vars[key] -= int(value)
        elif line.startswith("MUL"):
            parts = line.split()
            key = parts[1]
            value = parts[2]
            if value in vars:  # Check if 'value' is a variable name
                vars[key] *= vars[value]
            else:
                vars[key] *= int(value)
        elif line.startswith("JUMP"):
            parts = line.split()
            index = locations.get(parts[1])
            continue
        elif line.startswith("IF"):
            parts = line.split()
            key1 = vars.get(parts[1])
            key2 = vars.get(parts[3])
            if key2 is None:
                key2 = int(parts[3])
            operator = parts[2]
            if operator == "<" and key1 < key2:
                index = locations[parts[-1]]
                continue
            if operator == ">" and key1 > key2:
                index = locations[parts[-1]]
                continue
            if operator == ">=" and key1 >= key2:
                index = locations[parts[-1]]
                continue
            if operator == "<=" and key1 <= key2:
                index = locations[parts[-1]]
                continue
            if operator == "==" and key1 == key2:
                index = locations[parts[-1]]
                continue
            if operator == "!=" and key1 != key2:
                index = locations[parts[-1]]
                continue
        elif line.startswith("END"):
            return prints
        index += 1
    
    return prints

if __name__ == "__main__":
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)