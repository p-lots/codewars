def plane_seat(a):
    seat_section = int(a[:-1])
    seat_cluster = a[-1]
    if seat_section > 60 or seat_cluster not in 'ABCDEFGHK':
        return 'No Seat!!'
    ret_section = 'Front' if seat_section <= 20 else 'Middle' if seat_section <= 40 else 'Back'
    ret_cluster = 'Left' if seat_cluster in 'ABC' else 'Middle' if seat_cluster in 'DEF' else 'Right'
    return f'{ret_section}-{ret_cluster}'