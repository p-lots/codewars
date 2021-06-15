def get_score(player):
    norm_kill = player['norm_kill'] * 100
    assist = player['assist'] * 50
    damage = player['damage'] * 0.5
    healing = player['healing'] * 1
    streak = 2 ** player['streak']
    env_kill = player['env_kill'] * 500
    return norm_kill + assist + damage + healing + streak + env_kill

def scoring(array):
    if not array:
        return []
    return [player['name'] for player in sorted(array, key=get_score, reverse=True)]
