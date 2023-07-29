def compare(a, b):
    if sorted(str(a)) == sorted(str(b)):
        return "100%"
    
    for ch in str(a):
        if ch in str(b):
            return "50%"
        
    return "0%"
