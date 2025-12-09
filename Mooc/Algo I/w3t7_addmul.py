import re

def evaluate(data):
    pattern = r"(add|mul)\((\d+),(\d+)\)"

    def swap(match):
        op, x, y = match.groups() 
        if (x.lstrip("0") != x and x != "0") or (y.lstrip("0") != y and y != "0"): return match.group(0)
        x, y = int(x), int(y)
        if x <= 0 or y <= 0: return match.group(0)
        return str(x + y if op == "add" else x * y)

    return re.sub(pattern, swap, data)

if __name__ == "__main__":
    print(evaluate("add(1,2)")) # 3
    print(evaluate("aybabtu")) # aybabtu
    print(evaluate("mul(6,7),mul(7,191)")) # 42,1337
    print(evaluate("abadd(123,456)mulxmul(3,13)")) # ab579mulx39
    print(evaluate("mul()mul(13)mul(0,1)")) # mul()mul(13)mul(0,1)
    print(evaluate("mul(585,600)add(794,845)mul(393,651)mul(944,316)mul(714,210)")) # mul()mul(13)mul(0,1)
    print(evaluate("add()add(5)add(0,1)add(1,0)add(1,-1)add(-1,1)add(1, 2)add(1.5,2)add(01,2)")) # mul()mul(13)mul(0,1)

    data = "mul(6,7)"*10**5
    result = evaluate(data)
    print(len(result)) # 200000
    print(result[:20]) # 42424242424242424242
