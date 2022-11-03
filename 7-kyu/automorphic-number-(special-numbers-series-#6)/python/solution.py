def automorphic(n):
    return 'Automorphic' if str(n * n)[-len(str(n)):] == str(n) else 'Not!!'