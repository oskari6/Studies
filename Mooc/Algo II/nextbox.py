def find_boxes(boxes, products):
    boxes.sort()
    result = []
    used = [False] * len(boxes)

    def binary_search(x):
        left, right = 0, len(boxes) - 1
        best = -1
        while left <= right:
            mid = (left + right) // 2
            if boxes[mid] >= x:
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        while best != -1 and best < len(boxes) and used[best]:
            best += 1
        return best if best < len(boxes) else -1

    for product in products:
        idx = binary_search(product)
        if idx == -1:
            result.append(-1)
        else:
            used[idx] = True
            result.append(boxes[idx])

    return result
    

if __name__ == "__main__":
    print(find_boxes([4, 4, 6, 8], [5, 5, 4, 6, 1]))
    # [6, 8, 4, -1, 4]

    print(find_boxes([1, 2, 3, 4], [1, 1, 1, 1, 1]))
    # [1, 2, 3, 4, -1]

    print(find_boxes([2, 2, 2, 2], [1, 1, 1, 1, 1, 1]))
    # [2, 2, 2, 2, -1, -1]

    print(find_boxes([1, 1, 1, 1], [2, 2]))
    # [-1, -1]

    boxes = []
    products = []
    for i in range(10**5):
        boxes.append(i % 100 + 1)
        products.append(3 * i % 97 + 1)
    result = find_boxes(boxes, products)
    print(result[42]) # 30
    print(result[1337]) # 35
    print(result[-1]) # 100