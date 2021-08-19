def textin(strng):
    ret = []
    for word in strng.split():
        if word.lower() in ['too', 'two', 'to']:
            ret.append('2')
            continue
        i = 0
        temp = ''
        while i < len(word):
            if word[i:i + 3].lower() == 'too' or word[i:i + 3].lower() == 'two':
                temp += '2'
                i += 3
            elif word[i:i + 2].lower() == 'to':
                temp += '2'
                i += 2
            else:
                temp += word[i]
                i += 1
        ret.append(temp)
    return ' '.join(ret)
        
            
                
            
