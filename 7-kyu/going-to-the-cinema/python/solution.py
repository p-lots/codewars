from math import ceil

def movie(card, ticket, perc):
    ret = 1
    card_price = card + ticket * perc
    total_ticket = ticket
    while not (ceil(card_price) < total_ticket):
        ret += 1
        card_price += ticket * (perc ** ret)
        total_ticket += ticket
    return ret