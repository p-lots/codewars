def is_monotone(heights):
    return all(x <= y for x, y in zip(heights, heights[1:]))