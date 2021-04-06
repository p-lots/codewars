def who_is_online(friends):
    if not friends:
        return {}
    ret = {}
    for user in friends:
        if user['status'] == 'online':
            if user['last_activity'] > 10:
                if 'away' not in ret.keys():
                    ret['away'] = []
                ret['away'].append(user['username'])
            else:
                if 'online' not in ret.keys():
                    ret['online'] = []
                ret['online'].append(user['username'])
        elif user['status'] == 'offline':
            if 'offline' not in ret.keys():
                ret['offline'] = []
            ret['offline'].append(user['username'])
    return ret
