def shorten_to_date(long_date):
    comma = long_date.index(',')
    return long_date[:comma]