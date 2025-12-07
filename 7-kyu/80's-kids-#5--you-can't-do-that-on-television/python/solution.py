def bucket_of(said):
    slime_triggers = ['i don\'t know', 'slime']
    water_triggers = ['water', 'wet', 'wash']
    
    check_drop = lambda phrases: any(phrase in said.lower() for phrase in phrases)
    
    drop_water = check_drop(water_triggers)
    drop_slime = check_drop(slime_triggers)
    
    if drop_water and drop_slime:
        return 'sludge'
    elif drop_water:
        return 'water'
    elif drop_slime:
        return 'slime'
    return 'air'
