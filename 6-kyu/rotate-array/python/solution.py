def rotate(data, n):
    return [data[index % len(data)] for index in range(-n, -n + len(data))]
