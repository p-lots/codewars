def kill_monsters(health, monsters, damage):
    hits = (monsters - 1) // 3
    health -= damage * hits
    return 'hero died' if health <= 0 else f'hits: {hits}, damage: {damage * hits}, health: {health}'
