def fuel_price(litres, price_per_litre):
    return round(litres * (price_per_litre - min((litres // 2 * 0.05), 0.25)), 2)