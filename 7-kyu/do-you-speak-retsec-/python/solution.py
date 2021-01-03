def reverse_by_center(s):
    midpt = len(s) // 2 if len(s) % 2 == 1 else 0
    return s[midpt + 1:] + s[midpt] + s[:midpt] if midpt else s[(len(s) + 1) // 2:] + s[:(len(s) + 1 )// 2]
