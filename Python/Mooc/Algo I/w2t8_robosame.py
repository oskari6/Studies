def calculate(input, rules):
    state = 1
    tape = list("L" + input + "R")
    index = 0
    rules_dict = {(symbol, s): (new_symbol, new_state, action) for symbol, s, new_symbol, new_state, action in rules}
    
    for _ in range(1000):
        current_symbol = tape[index]
        key = (current_symbol, state)
        if key not in rules_dict: return False
            
        new_symbol, new_state, action = rules_dict[key]
        tape[index] = new_symbol
        state = new_state

        if action == "RIGHT":  index += 1
        elif action == "LEFT": index -= 1
        elif action == "ACCEPT": return True
        elif action == "REJECT":  return False
        if index < 0 or index >= len(tape): return False
            
    return False

def create_rules():
    rules = [
        ("L", 1, "L", 2, "RIGHT"),
        ("0", 2, "0", 3, "RIGHT"),
        ("1", 2, "1", 3, "RIGHT"),
        ("0", 3, "0", 4, "RIGHT"),
        ("1", 3, "1", 4, "RIGHT"),
        ("0", 4, "0", 5, "RIGHT"),
        ("1", 4, "1", 5, "RIGHT"),
        ("0", 5, "0", 6, "RIGHT"),
        ("1", 5, "1", 6, "RIGHT"),
        ("0", 6, "0", 7, "RIGHT"),
        ("1", 6, "1", 7, "RIGHT"),
        ("0", 7, "0", 8, "RIGHT"),
        ("1", 7, "1", 8, "RIGHT"),
        ("0", 8, "0", 9, "RIGHT"),
        ("1", 8, "1", 9, "RIGHT"),
        ("0", 9, "0", 10, "RIGHT"),
        ("1", 9, "1", 10, "RIGHT"),
        ("0", 10, "0", 11, "RIGHT"),
        ("1", 10, "1", 11, "RIGHT"),
        ("0", 11, "0", 12, "RIGHT"),
        ("1", 11, "1", 12, "RIGHT"),

        # Reject
        ("R", 2, "1", 1, "REJECT"),("R", 3, "1", 1, "REJECT"),
        ("R", 5, "1", 1, "REJECT"),("R", 7, "1", 1, "REJECT"),
        ("R", 9, "1", 1, "REJECT"),("R", 11, "1", 1, "REJECT"),
        # Accept
        ("R", 4, "R", 21, "LEFT"),("R", 6, "R", 31, "LEFT"),
        ("R", 8, "R", 41, "LEFT"),("R", 10, "R", 51, "LEFT"),
        ("R", 12, "R", 61, "LEFT"),

        # To middle 2
        ("0", 21, "0", 22, "LEFT"),
        ("1", 21, "1", 22, "LEFT"),
        ("0", 22, "0", 100, "RIGHT"),
        ("1", 22, "1", 99, "RIGHT"),
        ("L", 22, "L", 1, "ACCEPT"),

        # To R
        ("0", 100, "0", 100, "RIGHT"),
        ("1", 100, "1", 100, "RIGHT"),
        ("0", 99, "0", 99, "RIGHT"),
        ("1", 99, "1", 99, "RIGHT"),
        ("R", 100, "R", 98, "LEFT"),
        ("R", 99, "R", 97, "LEFT"),
        # Check last 2
        ("0", 98, "R", 21, "LEFT"),
        ("1", 97, "R", 21, "LEFT"),
        ("1", 98, "R", 1, "REJECT"),
        ("0", 97, "R", 1, "REJECT"),

        # To middle 4
        ("0", 31, "0", 32, "LEFT"),
        ("1", 31, "1", 32, "LEFT"),
        ("0", 32, "0", 33, "LEFT"),
        ("1", 32, "1", 33, "LEFT"),
        ("0", 33, "0", 96, "RIGHT"),
        ("1", 33, "1", 95, "RIGHT"),
        ("L", 33, "L", 1, "ACCEPT"),
        # To R
        ("0", 96, "0", 96, "RIGHT"),
        ("1", 96, "1", 96, "RIGHT"),
        ("0", 95, "0", 95, "RIGHT"),
        ("1", 95, "1", 95, "RIGHT"),
        ("R", 96, "R", 94, "LEFT"),
        ("R", 95, "R", 93, "LEFT"),
        # Check last 4
        ("0", 94, "R", 31, "LEFT"),
        ("1", 93, "R", 31, "LEFT"),
        ("1", 94, "R", 1, "REJECT"),
        ("0", 93, "R", 1, "REJECT"),

        # To middle 6
        ("0", 41, "0", 42, "LEFT"),
        ("1", 41, "1", 42, "LEFT"),
        ("0", 42, "0", 43, "LEFT"),
        ("1", 42, "1", 43, "LEFT"),
        ("0", 43, "0", 44, "LEFT"),
        ("1", 43, "1", 44, "LEFT"),
        ("0", 44, "0", 92, "RIGHT"),
        ("1", 44, "1", 91, "RIGHT"),
        ("L", 44, "L", 1, "ACCEPT"),
        # To R
        ("0", 92, "0", 92, "RIGHT"),
        ("1", 92, "1", 92, "RIGHT"),
        ("0", 91, "0", 91, "RIGHT"),
        ("1", 91, "1", 91, "RIGHT"),
        ("R", 92, "R", 90, "LEFT"),
        ("R", 91, "R", 89, "LEFT"),
        # Check last 6
        ("0", 90, "R", 41, "LEFT"),
        ("1", 89, "R", 41, "LEFT"),
        ("1", 90, "R", 1, "REJECT"),
        ("0", 89, "R", 1, "REJECT"),

        # To middle 8
        ("0", 51, "0", 52, "LEFT"),
        ("1", 51, "1", 52, "LEFT"),
        ("0", 52, "0", 53, "LEFT"),
        ("1", 52, "1", 53, "LEFT"),
        ("0", 53, "0", 54, "LEFT"),
        ("1", 53, "1", 54, "LEFT"),
        ("0", 54, "0", 55, "LEFT"),
        ("1", 54, "1", 55, "LEFT"),
        ("0", 55, "0", 88, "RIGHT"),
        ("1", 55, "1", 87, "RIGHT"),
        ("L", 55, "L", 1, "ACCEPT"),
        # To R
        ("0", 88, "0", 88, "RIGHT"),
        ("1", 88, "1", 88, "RIGHT"),
        ("0", 87, "0", 87, "RIGHT"),
        ("1", 87, "1", 87, "RIGHT"),
        ("R", 88, "R", 86, "LEFT"),
        ("R", 87, "R", 85, "LEFT"),
        # Check last 8
        ("0", 86, "R", 51, "LEFT"),
        ("1", 85, "R", 51, "LEFT"),
        ("1", 86, "R", 1, "REJECT"),
        ("0", 85, "R", 1, "REJECT"),

        # To middle 10
        ("0", 61, "0", 62, "LEFT"),
        ("1", 61, "1", 62, "LEFT"),
        ("0", 62, "0", 63, "LEFT"),
        ("1", 62, "1", 63, "LEFT"),
        ("0", 63, "0", 64, "LEFT"),
        ("1", 63, "1", 64, "LEFT"),
        ("0", 64, "0", 65, "LEFT"),
        ("1", 64, "1", 65, "LEFT"),
        ("0", 65, "0", 66, "LEFT"),
        ("1", 65, "1", 66, "LEFT"),
        ("0", 66, "0", 84, "RIGHT"),
        ("1", 66, "1", 83, "RIGHT"),
        ("L", 66, "L", 1, "ACCEPT"),
        # To R
        ("0", 84, "0", 84, "RIGHT"),
        ("1", 84, "1", 84, "RIGHT"),
        ("0", 83, "0", 83, "RIGHT"),
        ("1", 83, "1", 83, "RIGHT"),
        ("R", 84, "R", 82, "LEFT"),
        ("R", 83, "R", 81, "LEFT"),
        # Check last 10
        ("0", 82, "R", 61, "LEFT"),
        ("1", 81, "R", 61, "LEFT"),
        ("1", 82, "R", 1, "REJECT"),
        ("0", 81, "R", 1, "REJECT"),
    ]
    
    return rules

if __name__ == "__main__":
    rules = create_rules()
    print(calculate("0111101111", rules)) # False