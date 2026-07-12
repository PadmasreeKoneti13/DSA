prices = [7,1,3,4,2,6,5]
max_profit = 0
min_price = float("inf")
for price in prices:
    if price < min_price:
        min_price = price
    profit = price - min_price
    max_profit = max(max_profit, profit)
print(max_profit)

