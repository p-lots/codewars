def knight_or_knave(said):
    if isinstance(said, str):
        ret = eval(said)
    else:
        ret = said
    return 'Knight!' if ret else 'Knave! Do not trust.'
