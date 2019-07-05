def diff(arr):
    diff = 0
    max_at_index = 0
    for (i, item) in enumerate(arr):
        temp_arr = item.split('-')
        temp_arr = list(map(int, temp_arr))
        curr_diff = abs(temp_arr[0] - temp_arr[1])
        if curr_diff > diff:
        	diff = curr_diff
        	max_at_index = i
    return arr[max_at_index] if diff > 0 else False