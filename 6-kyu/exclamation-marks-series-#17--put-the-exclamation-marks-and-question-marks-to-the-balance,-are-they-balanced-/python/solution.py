def balance(left, right):
    lft = left.count('!') * 2 + left.count('?') * 3
    rgt = right.count('!') * 2 + right.count('?') * 3
    return "Left" if lft > rgt else "Balance" if lft == rgt else "Right"
  