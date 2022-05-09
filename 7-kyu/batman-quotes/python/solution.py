class BatmanQuotes(object):

    @staticmethod
    def get_quote(quotes, hero):
        for ch in hero:
            if ch.isdigit():
                idx = int(ch)
        if hero[0] == 'B':
            hero = 'Batman'
        elif hero[0] == 'J':
            hero = 'Joker'
        elif hero[0] == 'R':
            hero = 'Robin'
        return f'{hero}: {quotes[idx]}'
