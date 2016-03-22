__author__ = 'seungjin77.han'

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

if __name__ == '__main__':
    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))

    price_sorted = sorted(zip(prices.values(), prices.keys()))

    print min_price, max_price
    print price_sorted

    print(min(prices, key=lambda k: prices[k]))
    print(max(prices, key=lambda k: prices[k]))
