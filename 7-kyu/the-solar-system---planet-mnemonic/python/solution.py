def is_planet_mnemonic_correct(solar_system, mnemonic):
    if not solar_system and not mnemonic:
        return True
    solar_system_cleaned = [body[0] for body in solar_system if body != 'Asteroid']
    if solar_system_cleaned and not mnemonic:
        return False
    try:
        mnemonic_split = [word[0] for word in mnemonic.split(' ')]
        if len(solar_system_cleaned) != len(mnemonic_split):
            return False
        return all(lhs == rhs for lhs, rhs in zip(solar_system_cleaned, mnemonic_split))
    except:
        return True
