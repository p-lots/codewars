def sort_by_language(arr):
    return sorted(arr, key=lambda user: (user.get('language'), user.get('first_name')))
