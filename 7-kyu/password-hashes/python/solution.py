import hashlib

def pass_hash(strng):
    md5_pass = hashlib.md5()
    md5_pass.update(strng.encode())
    return md5_pass.hexdigest()