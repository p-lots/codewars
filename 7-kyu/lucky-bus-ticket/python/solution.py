def is_lucky(ticket):
    return sum(map(int, ticket[:3])) == sum(map(int, ticket[3:])) if len(ticket) == 6 and all(ch.isdigit() for ch in ticket) else False