def remove_url_anchor(url):
    try:
        anchor_index = url.index('#')
    except ValueError:
        return url
    return url[:anchor_index]