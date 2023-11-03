def max_profit(prices):
    # 개선된 방식
    max_profit = 0
    min_price = prices[0]
    
    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i]- min_price)
    return max_profit
    
max_profit([70, 30, 50, 10, 60, 40])