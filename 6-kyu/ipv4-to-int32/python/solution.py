def ip_to_int32(ip):
    return int(''.join(f'{int(octet):08b}' for octet in ip.split('.')), 2)
