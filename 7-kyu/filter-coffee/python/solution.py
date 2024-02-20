def search(budget, prices):
    prices = sorted(prices)
    return ','.join(str(price) for price in prices if price <= budget)
