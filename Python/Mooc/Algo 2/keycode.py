def find_codes(pattern):
    if "?" not in pattern: 
        return [pattern]
    codes = []

    for num in range(1234,9877):
        if check_valid(str(num)) and check_code(str(num), pattern):
            codes.append(str(num))
    return codes

def check_code(num, code):
    for i in range(len(code)):
        if code[i] == "?":
            continue
        if num[i] != code[i]:
            return False
    return True

def check_valid(number):
    if len(set(number)) == 4 and "0" not in number:
        return True
    return False

if __name__ == "__main__":
    codes = find_codes("24?5")
    print(codes) # ['2415', '2435', '2465', '2475', '2485', '2495']

    codes = find_codes("1?2?")
    print(codes[:5]) # ['1324', '1325', '1326', '1327', '1328']
    print(len(codes)) # 42

    codes = find_codes("????")
    print(codes[:5]) # ['1234', '1235', '1236', '1237', '1238']
    print(len(codes)) # 3024
    
    codes = find_codes("3148")
    print(codes)