from collections import deque

def min_amount(left_volume, right_volume, target):
    visited = set()
    queue = deque()
    queue.append((0,0,0)) #meaning (left,right,moved amount)
    visited.add((0,0))

    while queue:
        left,right,moved = queue.popleft()
        if left == target: return moved
        next_states = []

        if left < left_volume: next_states.append((left_volume, right, moved+(left_volume-left)))
        if right < right_volume: next_states.append((left, right_volume, moved+(right_volume-right)))
        if left > 0: next_states.append((0, right, moved+left))
        if right > 0: next_states.append((left, 0, moved+right))

        pour  = min(left, right_volume - right)
        if pour > 0: next_states.append((left-pour,right+pour, moved+pour))

        pour = min(right, left_volume-left)
        if pour > 0: next_states.append((left+pour,right-pour, moved+pour))

        for new_l, new_r, new_m in next_states:
            if(new_l, new_r) not in visited:
                if (new_l == 0 or new_l == left_volume
                    or new_r == 0 or new_r == right_volume):
                    visited.add((new_l, new_r))
                    queue.append((new_l, new_r, new_m))

    return -1

if __name__ == "__main__":
    print(min_amount(5, 4, 2)) # 22
    print(min_amount(4, 3, 2)) # 16
    print(min_amount(3, 3, 1)) # -1
    print(min_amount(1, 1, 10**9)) # -1
    print(min_amount(10, 9, 8)) # 46
    print(min_amount(123, 456, 42)) # 10530