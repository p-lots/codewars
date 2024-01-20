def html_special_chars(data):
    replacements = {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}
    for to_replace, replacement in replacements.items():
        data = data.replace(to_replace, replacement)
    return data