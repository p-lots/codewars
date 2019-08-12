def say_hello(name, city, state):
    name_joined = ' '.join(name)
    return 'Hello, {0}! Welcome to {1}, {2}!'.format(name_joined, city, state)