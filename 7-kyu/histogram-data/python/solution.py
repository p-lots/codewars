def histogram(values: list[int], bin_width: int) -> list[int]:
    if not values:
        return []
    bucket_count = max(values) // bin_width + 1
    return [sum(values.count(j) for j in range(i * bin_width, i * bin_width + bin_width)) for i in range(bucket_count)]