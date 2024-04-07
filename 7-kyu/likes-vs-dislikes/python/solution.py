def like_or_dislike(lst):
    ret = 'Nothing'
    for button_press in lst:
        if button_press == 'Like':
            if ret == 'Nothing' or ret == 'Dislike':
                ret = 'Like'
            elif ret == 'Like':
                ret = 'Nothing'
        elif button_press == 'Dislike':
            if ret == 'Nothing' or ret == 'Like':
                ret = 'Dislike'
            elif ret == 'Dislike':
                ret = 'Nothing'
    return ret
