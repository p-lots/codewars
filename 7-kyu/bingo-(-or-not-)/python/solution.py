def bingo(array): 
    winning_numbers = [ord(ch) - ord('A') + 1 for ch in 'BINGO'] # A = 1, B = 2, ...
    return 'WIN' if all(num in array for num in winning_numbers) else 'LOSE'