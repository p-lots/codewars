def warn_the_sheep(queue):
    wolf_idx = queue.index('wolf')
    return 'Pls go away and stop eating my sheep' if wolf_idx == len(queue) - 1 else 'Oi! Sheep number {0}! You are about to be eaten by a wolf!'.format(len(queue) - wolf_idx - 1)