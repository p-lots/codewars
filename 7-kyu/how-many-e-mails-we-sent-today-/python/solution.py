def get_percentage(sent, limit=1000):
    if sent == 0:
        return 'No e-mails sent'
    elif sent >= limit:
        return 'Daily limit is reached'
    percentage = int(sent / limit * 100)
    return f'{percentage}%'