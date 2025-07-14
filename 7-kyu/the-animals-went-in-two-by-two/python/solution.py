def two_by_two(animals):
    return {animal: 2 for animal in animals if animals.count(animal) > 1} if animals else False