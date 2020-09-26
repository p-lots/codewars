import hashlib

def crack(hash):
    test_pin = 0
    test_hash = hashlib.md5(str(test_pin).zfill(5).encode('utf-8')).hexdigest()
    while test_hash != hash:
        test_pin += 1
        test_hash = hashlib.md5(str(test_pin).zfill(5).encode('utf-8')).hexdigest()
    return str(test_pin).zfill(5)