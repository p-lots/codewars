def top3(products, amounts, prices):
    zipped = sorted(zip(products, amounts, prices), key=lambda item: item[1] * item[2], reverse=True)
    return [item[0] for item in zipped[:3]]