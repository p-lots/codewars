def cut_fruits(fruits):
    ret = []
    for item in fruits:
        if item in FRUIT_NAMES:
            halfway = len(item) // 2
            if len(item) % 2 == 1:
                halfway += 1
            part1, part2 = item[:halfway], item[halfway:]
            ret.append(part1)
            ret.append(part2)
        else:
            ret.append(item)
    return ret