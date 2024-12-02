from datetime import datetime

def is_it_valid(pic):
    if len(pic) != 11:
        return False
    
    control_string= "0123456789ABCDEFHJKLMNPRSTUVWXY"
    century = pic[6]
    date = pic[0:6]
    if century == "+":
        century = "18"
    elif century == "-":
        century = "19"
    elif century == "A":
        century = "20"
    else:
        return False
    
    try:
        day = int(date[0:2])
        month = int(date[2:4])
        year = int(century + date[4:6])

        datetime(year, month, day)
    except ValueError:
        return False

    personal = pic[7:10]
    control_char = pic[10]
    control_num = int(pic[:6] + pic[7:10]) % 31
    control_char_test = control_string[control_num]
    if control_char != control_char_test:
        return False

    return True

if __name__ == "__main__":
    print(is_it_valid("310286+713J"))