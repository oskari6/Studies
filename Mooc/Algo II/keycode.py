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

def evaluate(code1, code2):
    in_place = sum(a == b for a, b in zip(code1, code2))
    in_code = sum(min(code1.count(d), code2.count(d)) for d in set(code1)) - in_place
    return (in_place, in_code)

def find_code(oracle):
    digits = "123456789"
    candidates = ["".join(p) for p in itertools.permutations(digits, 4)]
    
    for _ in range(16):
        guess = candidates[0]
        feedback = oracle.check_code(guess)
        if feedback == (4, 0):
            return guess
        
        candidates = [code for code in candidates if evaluate(guess, code) == feedback]
    
    raise RuntimeError("Failed to find the code within 16 queries")

if __name__ == "__main__":
    # example of using the oracle
    oracle = Oracle("4217")
    print(oracle.check_code("1234")) # (1, 2)
    print(oracle.check_code("3965")) # (0, 0)
    print(oracle.check_code("4271")) # (2, 2)
    print(oracle.check_code("4217")) # (4, 0)

    # example of using the function find_code
    oracle = Oracle("4517")
    code = find_code(oracle)
    print(code) # 4217
