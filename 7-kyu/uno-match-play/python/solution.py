def can_play(hand, face_up):
    color, number = face_up.split(' ')
    return any(color in card or number in card for card in hand)
