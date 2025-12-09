def create_string(pages):
    if not pages: return ""
    if len(pages) < 2:  return str(pages[0])
    pages = sorted(set(pages))
    result = []
    start = pages[0]
    prev = pages[0]

    for i in range(1,len(pages)):
        if pages[i] == prev + 1:  prev = pages[i]
        else:
            if start == prev: result.append(str(start))
            else: result.append(f"{start}-{prev}")
            start = prev = pages[i]
    
    if start == prev: result.append(str(start))
    else: result.append(f"{start}-{prev}")
    return ",".join(result)

if __name__ == "__main__":
    print(create_string([1])) # 1
    print(create_string([1, 2, 3])) # 1-3
    print(create_string([1, 1, 1])) # 1
    print(create_string([1, 2, 1, 2])) # 1-2
    print(create_string([1, 6, 2, 5])) # 1-2,5-6
    print(create_string([1, 3, 5, 7])) # 1,3,5,7
    print(create_string([1, 8, 2, 7, 3, 6, 4, 5])) # 1-8
    print(create_string([3, 2, 9, 4, 3, 6, 9, 8])) # 2-4,6,8-9

    pages = [3, 2, 1, 3, 2, 1]
    print(create_string(pages)) # 1-3
    print(pages) # [3, 2, 1, 3, 2, 1]