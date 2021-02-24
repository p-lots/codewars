def michael_pays(costs):
    return round(costs - min(costs * (1 / 3), 10), 2) if costs >= 5 else round(costs, 2)
