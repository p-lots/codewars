def search_names(logins):
    return filter(lambda elem: elem[0][-1] == '_', logins)