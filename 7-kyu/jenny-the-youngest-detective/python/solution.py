def missing(nums, s):
    s = ''.join(s.split())
    return ''.join(s[num].lower() for num in sorted(nums)) if max(nums) < len(s) else 'No mission today'
