def find_distances(street):
    length = len(street)
    distances = [float("inf")]*length
    last_shop = -float("inf")
    for i in range(length):
        if street[i] == "1": last_shop = i
        distances[i] = min(distances[i], i - last_shop)

    last_shop = float("inf")
    for i in range(length-1, -1, -1):
        if street[i] == "1": last_shop = i
        distances[i] = min(distances[i], last_shop - i)

    return distances

if __name__ == "__main__":
    print(find_distances("00100010")) # [2, 1, 0, 1, 2, 1, 0, 1]
    print(find_distances("00100000")) # [2, 1, 0, 1, 2, 3, 4, 5]
    print(find_distances("11111111")) # [0, 0, 0, 0, 0, 0, 0, 0]
    print(find_distances("01010101")) # [1, 0, 1, 0, 1, 0, 1, 0]
    print(find_distances("10000000")) # [0, 1, 2, 3, 4, 5, 6, 7]
    print(find_distances("00000001")) # [7, 6, 5, 4, 3, 2, 1, 0]

    n = 10**5
    street = "0"*n + "1" + "0"*n
    distances = find_distances(street)
    print(distances[1337]) # 98663