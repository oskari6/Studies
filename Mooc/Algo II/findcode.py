import itertools
import re
import time
 
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
 
import itertools

def get_feedback(secret, guess):
    in_place = sum(a == b for a, b in zip(secret, guess))
    in_code = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - in_place
    return in_place, in_code

def find_code(oracle):
    # Step 1: Generate all valid permutations of 4-digit codes (1-9, unique digits)
    digits = '123456789'
    candidates = [''.join(p) for p in itertools.permutations(digits, 4)]

    for attempt in range(16):
        guess = candidates[0]
        in_place, in_code = oracle.check_code(guess)

        if in_place == 4:
            return guess

        # Step 2: Filter out incompatible candidates
        candidates = [
            code for code in candidates
            if get_feedback(code, guess) == (in_place, in_code)
        ]

    return None  # If not found within 16 tries

if __name__ == "__main__":
    # example of using the function find_code
    
    start_time = time.perf_counter()
    oracle = Oracle("9876")
    code = find_code(oracle)
    print(code) # 4217
    end_time = time.perf_counter()
    print(f"1. time: {end_time - start_time:.6f} s")