def _if(b, func1, func2):
    return func1() if b else func2()