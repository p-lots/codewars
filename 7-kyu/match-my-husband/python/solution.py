def match(usefulness, months):
    usefulness_total = sum(usefulness)
    needs_starting = 100
    decay = 0.15
    needs = needs_starting * (1 - decay) ** months
    return "Match!" if usefulness_total >= needs else "No match!"