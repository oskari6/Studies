import heapq

def find_steps(numbers):
    n = len(numbers)
    if n == 0: return -1

    dist = [float("inf")] * n
    dist[0] = 0
    heap = [(0,0)]

    while heap:
        cost,i = heapq.heappop(heap)

        if i == n -1:return cost

        x = numbers[i]
        for next_i in [i-x,i+x]:
            if 0 <= next_i < n:
                new_cost = cost+x
                if new_cost < dist[next_i]:
                    dist[next_i] = new_cost
                    heapq.heappush(heap, (new_cost, next_i))

    return -1

if __name__ == "__main__":
    print(find_steps([1, 1, 1, 1])) # 3
    print(find_steps([3, 2, 1])) # -1
    print(find_steps([3, 5, 2, 2, 2, 3, 5])) # 10
    print(find_steps([7, 5, 3, 1, 4, 2, 4, 6, 1])) # 32

    numbers = []
    for i in range(10**5):
        numbers.append(1337 * i % 100 + 1)
    print(find_steps(numbers)) # 100055