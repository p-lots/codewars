def is_ruby_coming(lst): 
    return any(elem['language'] == 'Ruby' for elem in lst)
