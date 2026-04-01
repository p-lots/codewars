# import datetime as dt
from datetime import timedelta, datetime

def life_predictor(birthdate):
    parsed_bday = datetime.strptime(birthdate, '%Y-%m-%d')
    GESTATION_LEN = timedelta(days=280)
    conception_day = parsed_bday - GESTATION_LEN
    return datetime.strftime(conception_day, '%Y-%m-%d')
