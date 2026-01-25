def merge_sorted(a,b):
    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if(a[i] <= b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])
    return result

# O(n+m)
if __name__ == "__main__":
    list1 = [1,5,7]
    list2 = [2,3,4]
    result = merge_sorted(list1, list2)
    print(result)