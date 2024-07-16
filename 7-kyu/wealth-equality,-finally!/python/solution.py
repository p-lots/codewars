def redistribute_wealth(wealth):
    new_wealth = sum(wealth) / len(wealth)
    for i in range(len(wealth)):
        wealth[i] = new_wealth
