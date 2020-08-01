def reject(seq, predicate): 
    return [elem for elem in seq if not predicate(elem)]