def rain_amount(rain_amount):
    return f'You need to give your plant {40 - rain_amount}mm of water' if rain_amount < 40 \
        else 'Your plant has had more than enough water for today!'