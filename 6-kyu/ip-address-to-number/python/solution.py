def ip_to_num(ip):
    octets = [f'{int(octet):08b}' for octet in ip.split('.')]
    joined = ''.join(octets)
    return int(joined, 2)

def num_to_ip(num):
    num_bin = f'{num:b}'.zfill(32)
    octets = [f'{int(num_bin[idx:idx + 8], 2)}' for idx in range(0, len(num_bin), 8)]
    return '.'.join(octets)
