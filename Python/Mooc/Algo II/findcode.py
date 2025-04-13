import itertools
import re
 
class Oracle:
    def __init__(self, code):
        self.code = code
        self.counter = 0
 
    def check_code(self, code):
        self.counter += 1
        if self.counter > 16:
            raise RuntimeError("too many check_code calls")
 
        if type(code) != str or not re.match("^[1-9]{4}$", code) or len(code) != len(set(code)):
            raise RuntimeError("invalid code for check_code")
 
        in_place = in_code = 0
        for pos in range(4):
            if code[pos] in self.code:
                if code[pos] == self.code[pos]:
                    in_place += 1
                else:
                    in_code += 1
 
        return in_place, in_code
 
def find_code(oracle):
    digit_groups = ["1234", "5678", "1290"]
    found_digits = set()

    for group in digit_groups:
        guess = "".join(d for d in group if d != "0")
        response = oracle.check_code(guess)
        if response[0] + response[1] > 0:
            for d in guess:
                found_digits.add(d)
        if len(found_digits) >= 4:
            break
    
    if len(found_digits) > 4:
        for combo in itertools.combinations(found_digits, 4):
            guess = "".join(combo)
            response = oracle.check_code(guess)
            if response[0] + response[1] == 4:
                found_digits = set(combo)
                break
    
    for perm in itertools.permutations(found_digits, 4):
        guess = "".join(perm)
        response = oracle.check_code(guess)
        if response == (4,0):
            return guess
        
    raise RuntimeError("Failed to find the code within 16 queries")
 
if __name__ == "__main__":
    # example of using the function find_code
    oracle = Oracle("9124")
    code = find_code(oracle)
    print(code) # 4217