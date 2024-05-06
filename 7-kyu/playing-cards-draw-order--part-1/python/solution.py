def draw(deck):
    drawn_cards = []
    i = 0
    while deck:
        top_card = deck.pop(0)
        if i % 2 == 0:
            drawn_cards.append(top_card)
        else:
            deck.append(top_card)
        i += 1
    return drawn_cards
