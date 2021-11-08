def sp_eng(sentence): 
    for i in range(len(sentence)):
        if sentence[i:i + len('english')].lower() == 'english':
            return True
    return False
