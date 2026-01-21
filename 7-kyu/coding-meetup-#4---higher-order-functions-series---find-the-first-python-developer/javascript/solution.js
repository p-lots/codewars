def get_first_python(users):
    ret = [f"{user['first_name']}, {user['country']}" for user in users if user['language'] == 'Python']
    return ret[0] if ret else 'There will be no Python developers'
