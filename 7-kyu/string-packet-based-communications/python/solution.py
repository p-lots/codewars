def communication_module(packet):
    header = packet[0:4]
    instruction = packet[4:8]
    data_p1 = int(packet[8:12])
    data_p2 = int(packet[12:16])
    footer = packet[16:]
    ret = ''
    if instruction == '0F12':
        ret = str(min(data_p1 + data_p2, 9999))
    elif instruction == 'B7A2':
        ret = str(max(data_p1 - data_p2, 0))
    elif instruction == 'C3D9':
        ret = str(min(data_p1 * data_p2, 9999))
    ret = header + 'FFFF' + ret.zfill(4) + '0000' + footer
    return ret