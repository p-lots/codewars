from collections import defaultdict

def who_is_online(friends):
    if not friends:
        return {}
    friends_status = defaultdict(list)
    for user in friends:
        username = user['username']
        if user['status'] == 'online':
            if user['last_activity'] > 10:
                friends_status['away'].append(username)
                continue
            friends_status['online'].append(username)
            continue
        friends_status['offline'].append(username)
    return friends_status