def find_profits(prices):
    profits = []
    best_buy_day = 0

    for cur_day, cur_price in enumerate(prices):
        profit = cur_price - prices[best_buy_day] + (cur_day - best_buy_day)
        if cur_price - prices[cur_day] > cur_price - prices[best_buy_day] + (cur_day - best_buy_day):
            best_buy_day = cur_day

        profits.append(max(0, profit))

    return profits

if __name__ == "__main__":
    print(find_profits([1, 2, 3, 4])) # [0, 2, 4, 6]
    print(find_profits([4, 3, 2, 1])) # [0, 0, 0, 0]
    print(find_profits([1, 1, 1, 1])) # [0, 1, 2, 3]
    print(find_profits([2, 4, 1, 3])) # [0, 3, 1, 4]
    print(find_profits([1, 1, 5, 1])) # [0, 1, 6, 3]
    print(find_profits([3, 2, 3, 5, 1, 4])) # [0, 0, 2, 5, 2, 6]
    print(find_profits([9, 6, 10, 10, 3, 6, 7, 6, 5, 7])) # [0, 0, 5, 6, 0, 4, 6, 6, 6, 9]
    print(find_profits([9, 6, 10, 10])) # [0, 0, 5, 6]

    prices = list(range(1, 10**5+1))
    print(find_profits(prices)[:5]) # [0, 2, 4, 6, 8]