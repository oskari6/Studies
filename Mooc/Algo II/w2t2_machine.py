def min_steps(x):
    if x < 1: return -1
    results = {}

    for i in range(1, x+1):
        results[i] = float("inf")
    
    results[1] = 0

    for i in range(2, x+1):
        if i % 2 == 0 and i // 2 in results:
            results[i] = min(results[i], results[i // 2] +1)
        if i -3 in results:
            results[i] = min(results[i], results[i-3] +1)
            
    return results[x] if results[i] != float("inf") else -1

if __name__ == "__main__":
    print(min_steps(1)) # 0
    print(min_steps(2)) # 1
    print(min_steps(3)) # -1
    print(min_steps(4)) # 1
    print(min_steps(5)) # 2
    print(min_steps(17)) # 4
    print(min_steps(42)) # -1
    print(min_steps(100)) # 7
    print(min_steps(1000)) # 13