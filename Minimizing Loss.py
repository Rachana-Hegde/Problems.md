def minimize_loss(prices):
    min_loss = float('inf')
    buy_year = sell_year = -1
    n = len(prices)

    for i in range(n):
        for j in range(i + 1, n):
            if prices[j] < prices[i]:
                loss = prices[i] - prices[j]
                if loss < min_loss:
                    min_loss = loss
                    buy_year, sell_year = i + 1, j + 1

    return buy_year, sell_year, min_loss

if __name__ == "__main__":
    prices = list(map(int, input("Enter space-separated prices (e.g. 20 15 7 2 13): ").split()))
    buy, sell, loss = minimize_loss(prices)
    if buy == -1:
        print("No valid loss found.")
    else:
        print(f"Buy in year {buy}, sell in year {sell}, loss: {loss}")
