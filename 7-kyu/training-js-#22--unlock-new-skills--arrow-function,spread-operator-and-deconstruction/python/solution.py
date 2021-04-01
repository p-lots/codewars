def shuffle_it(arr, *swaps):
    for swap in swaps:
        arr[swap[0]], arr[swap[1]] = arr[swap[1]], arr[swap[0]]
    return arr
