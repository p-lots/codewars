def get_first_python(users):
    result = [f'{user["first_name"]}, {user["country"]}' for user in users if user['language'] == 'Python']
    return 'There will be no Python developers' if not result else result[0]
