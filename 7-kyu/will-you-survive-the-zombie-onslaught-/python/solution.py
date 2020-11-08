def zombie_shootout(zombies, distance, ammo):
    if zombies == 0:
        return "You shot all 0 zombies."
    zombs = zombies
    while distance > 0 and ammo > 0:
        zombs -= 1
        if zombs == 0:
            return f"You shot all {zombies} zombies."
        distance -= 0.5
        ammo -= 1
    if ammo == 0 and distance > 0:
        return f"You shot {zombies - zombs} zombies before being eaten: ran out of ammo."
    return f"You shot {zombies - zombs} zombies before being eaten: overwhelmed."