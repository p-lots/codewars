def replace_all(obj, find, replace):
    if isinstance(obj, list):
        return [replace if elem == find else elem for elem in obj]
    elif isinstance(obj, str):
        return obj.replace(find, replace)
