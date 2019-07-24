def discover_original_price(discounted_price, sale_percentage):
    return float('{0:.2f}'.format(discounted_price / (1 - sale_percentage / 100)))