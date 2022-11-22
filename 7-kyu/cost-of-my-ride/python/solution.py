def insurance(age, size, num_of_days):
    age_charge = 10 * (age < 25)
    size_table = {'economy': 0, 'medium': 10, 'full-size': 15}
    size_charge = size_table.get(size, 15)
    return max(num_of_days, 0) * (50 + age_charge + size_charge)
