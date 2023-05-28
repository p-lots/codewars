def cannons_ready(gunners):
    return 'Fire!' if all(val == 'aye' for val in gunners.values()) else 'Shiver me timbers!'
