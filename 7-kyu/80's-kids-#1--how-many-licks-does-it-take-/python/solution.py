def total_licks(env):
    licks_base = 252
    total_licks = sum(env.values())
    additional_challenge = ''
    if any(l > 0 for l in env.values()):
        chal_type = list(env.keys())[0]
        greatest_licks = list(env.values())[0]
        for chal, licks in env.items():
            if licks > greatest_licks:
                chal_type = chal
                greatest_licks = licks
        additional_challenge = f' The toughest challenge was {chal_type}.'
    return f'It took {licks_base + total_licks} licks to get to the tootsie roll center of a tootsie pop.{additional_challenge}'
