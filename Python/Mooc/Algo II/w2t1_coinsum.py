def can_create(coins, target):
    results = {}

    results[0] = 1
    for i in range(1,target+1):
        results[i] = 0
        for coin in coins:
            if i - coin >= 0:
                results[i] += results[i - coin]

    return True if results[target] > 0 else False

if __name__ == "__main__":
    print(can_create([1, 2, 5], 13)) # True
    print(can_create([2, 4, 6], 13)) # False
    print(can_create([1], 42)) # True
    print(can_create([2, 4, 6], 42)) # True
    print(can_create([3], 1337)) # False
    print(can_create([3, 4], 1337)) # True