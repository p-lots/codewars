def list_animals(animals):
    listed = [f'{idx + 1}. {animal}\n' for idx, animal in enumerate(animals)]
    return ''.join(listed)