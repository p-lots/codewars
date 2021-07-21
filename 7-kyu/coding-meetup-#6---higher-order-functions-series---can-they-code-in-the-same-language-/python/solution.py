def is_same_language(lst): 
    return all(entry['language'] == lst[0]['language'] for entry in lst)
