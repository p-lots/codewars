def change_me(money): 
    match money:
        case '£5':
            return ('20p ' * 25)[:-1]
        case '£2':
            return ('20p ' * 10)[:-1]
        case '£1':
            return ('20p ' * 5)[:-1]
        case '50p':
            return '20p 20p 10p'
        case '20p':
            return '10p 10p'
        case _:
            return money