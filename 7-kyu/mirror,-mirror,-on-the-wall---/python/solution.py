def mirror(data: list) -> list:
    if not data or len(data) == 1:
        return data
    dta = sorted([elem for elem in data])
    return dta + dta[-2::-1]
