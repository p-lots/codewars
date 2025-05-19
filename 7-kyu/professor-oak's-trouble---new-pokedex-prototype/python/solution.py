class PokeScan:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type
    
    def info(self):
        if self.level <= 20:
            level_desc = 'weak'
        elif self.level <= 50:
            level_desc = 'fair'
        else:
            level_desc = 'strong'
        match self.type:
            case 'water':
                type_desc = 'wet'
            case 'fire':
                type_desc = 'fiery'
            case 'grass':
                type_desc = 'grassy'
            case _:
                type_desc = ''
        return f'{self.name}, a {type_desc} and {level_desc} Pokemon.'
