from urllib.parse import quote

def generate_link(user):
    base_url = 'http://www.codewars.com/users/'
    return f'{base_url}{quote(user)}'
