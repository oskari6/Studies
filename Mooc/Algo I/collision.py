def hash_value(string): 
    """ Compute hash using sequential multiplication by A=23 mod M """
    A = 23
    M = 2**32
    hash_val = 0
    for char in string:
        hash_val = (hash_val * A + ord(char)) % M
    return hash_val

def find_other(string):
    
if __name__ == "__main__":
    string1 = "a"
    string2 = find_other(string1)
    print(string1, hash_value(string1))
    print(string2, hash_value(string2))
