def change_case(orig_string: str)->str:
    new = []
    for letter in orig_string:
        if letter.islower():
            new.append(letter.upper())
        else:
            new.append(letter.lower())

    return "".join(new)

def split_in_half(orig_string: str) -> tuple:
    index = len(orig_string) // 2
    first, second = orig_string[:index], orig_string[index:] 
    return first, second

def remove_special_characters(orig_string: str) -> str:
    specials = "!#%&/()=?*§:;.,<>_-+¤"
    for special in specials:
        orig_string = orig_string.replace(special, "")
    return orig_string