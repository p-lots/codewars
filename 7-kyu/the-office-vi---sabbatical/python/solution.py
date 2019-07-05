def sabb(s, value, happiness):
    ret = value + happiness + sum(1 for ch in s.lower() if ch in 'sabticl')
    return 'Sabbatical! Boom!' if ret > 22 else 'Back to your desk, boy.'