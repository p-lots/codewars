def tacofy(word):
    INGREDIENTS = {'a': 'beef', 'e': 'beef', 'i': 'beef',
                   'o': 'beef', 'u': 'beef', 't': 'tomato',
                   'l': 'lettuce', 'c': 'cheese', 'g': 'guacamole',
                   's': 'salsa'}
    return ['shell'] + [INGREDIENTS.get(ch) for ch in word.lower() if ch in INGREDIENTS] + ['shell']
