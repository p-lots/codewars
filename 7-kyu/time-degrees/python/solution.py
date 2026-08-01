def clock_degree(s) :
    hh, mm = map(int, s.split(':'))
    if not 0 <= hh <= 23 or not 0 <= mm <= 59:
        return 'Check your time !'
    h_deg = int((360 / 12) * (12 if hh == 0 or hh == 12 else hh % 12))
    m_deg = int((360 / 60) * (60 if mm == 0 else mm))
    return f'{h_deg}:{m_deg}'
