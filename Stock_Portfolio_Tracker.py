stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 330
}

total = 0
portfolio = {}

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock in stock_prices:
        qty = int(input(f"Enter quantity of {stock}: "))
        cost = stock_prices[stock] * qty
        portfolio[stock] = cost
        total += cost
    else:
        print("Stock not found.")

print("📊 Total Investment:", total)

with open("portfolio.txt", "w") as f:
    for s, c in portfolio.items():
        f.write(f"{s}: ${c}\n")
    f.write(f"Total: ${total}")
