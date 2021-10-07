def task(w, n, c):
    worker_lookup = {'Monday': 'James', 'Tuesday': 'John', 'Wednesday': 'Robert', 'Thursday': 'Michael', 'Friday': 'William'}
    return f'It is {w} today, {worker_lookup[w]}, you have to work, you must spray {n} trees and you need {n * c} dollars to buy liquid'
