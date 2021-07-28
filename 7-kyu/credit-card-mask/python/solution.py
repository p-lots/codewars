def maskify(cc):
    return cc if len(cc) <= 4 else f'{"#" * (len(cc) - 4)}{cc[-4:]}'
