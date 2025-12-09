import random
import re

from itertools import permutations

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

def filter_codes(code1, code2):
    in_place = sum(a == b for a, b in zip(code1, code2))
    in_code = sum(min(code1.count(d), code2.count(d)) for d in set(code1)) - in_place
    return (in_place, in_code)

def find_code(oracle):
    candidates = [''.join(p) for p in permutations('123456789', 4)]

    for _ in range(16):
        guess = candidates[0] if len(candidates) < 50 else candidates[len(candidates) // 2]
        result = oracle.check_code(guess)
        if result == (4, 0):
            return guess

        candidates = [c for c in candidates if filter_codes(guess, c) == result]

        if len(candidates) == 1: return candidates[0]

    return 0

if __name__ == "__main__":
    # example of using the function find_code
    rand = "".join(random.sample("123456789",4))
    oracle = Oracle(rand)
    code = find_code(oracle)
    print(code) # 4217
    print(oracle.code)