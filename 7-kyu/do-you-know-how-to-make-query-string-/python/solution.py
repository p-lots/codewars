def to_query_string(data):
    ret = []
    for key, value in data.items():
        if isinstance(value, list):
            for elem in value:
                ret.append(f'{key}={elem}')
        else:
            ret.append(f'{key}={value}')
    return '&'.join(ret)
