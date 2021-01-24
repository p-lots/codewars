def rake_garden(garden):
    return ' '.join('rock' if elem == 'rock' else 'gravel' for elem in garden.split())