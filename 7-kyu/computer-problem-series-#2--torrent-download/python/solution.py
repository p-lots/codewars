def time_to_dl(item):
    return (item['size_GB'] * 8000 * (1 / item['speed_Mbps']), item['name'])

def torrent(files): 
    files_sorted = sorted(files, key=time_to_dl)
    return ([item['name'] for item in files_sorted], time_to_dl(files_sorted[-1])[0])