from itertools import permutations

def min_count(weights, max_weight):
    if not weights: return 0

    for weight in weights:
            if weight > max_weight:
                return -1

    weights = sorted(weights, reverse=True) 
    min_count = len(weights)

    for perm in permutations(weights):  
        boxes = []
        for weight in perm:
            placed = False
            for i in range(len(boxes)):
                if boxes[i] + weight <= max_weight:
                    boxes[i] += weight
                    placed = True
                    break
            if not placed:
                boxes.append(weight)

        min_count = min(min_count, len(boxes))

    return min_count

if __name__ == "__main__":
    print(min_count([2, 3, 3, 5], 7))  # 2
    print(min_count([2, 3, 3, 5], 6))  # 3
    print(min_count([2, 3, 3, 5], 5))  # 3
    print(min_count([2, 3, 3, 5], 4))  # -1
    print(min_count([], 1))  # 0
    print(min_count([1], 1))  # 1
    print(min_count([1, 1, 1, 1], 1))  # 4
    print(min_count([1, 1, 1, 1], 4))  # 1
    print(min_count([3, 4, 1, 2, 3, 3, 5, 9], 10))  # 3