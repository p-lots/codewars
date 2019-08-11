def find_children(santas_list, children):
    children = set(children)
    return sorted(list(set([child for child in santas_list if child in children])))