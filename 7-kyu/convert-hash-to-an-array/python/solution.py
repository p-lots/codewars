def convert_hash_to_array(hash):
    return sorted([[k, v] for k, v in hash.items()], key=lambda elem: elem[0])