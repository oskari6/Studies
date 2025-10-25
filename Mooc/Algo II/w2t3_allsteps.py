def count_steps(x):
    if x < 1: return 0

    results = {}
    for i in range(1, x + 1): results[i] = 0
        
    results[1] = 1

    for i in range(2, x + 1):
        if i % 2 == 0:
            results[i] += results[i // 2]
        if i - 3 >= 1:
            results[i] += results[i - 3]

    return results[x]

if __name__ == "__main__":
    print(count_steps(1)) # 1
    print(count_steps(2)) # 1
    print(count_steps(3)) # 0
    print(count_steps(4)) # 2
    print(count_steps(5)) # 1
    print(count_steps(17)) # 5
    print(count_steps(42)) # 0
    print(count_steps(100)) # 242
    print(count_steps(1000)) # 2948311