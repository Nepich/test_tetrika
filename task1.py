def task1(array):
    if isinstance(array, str):
        return array.find('0')
    else:
        return array.index(0)


def task11(x1, y1, x2, y2, x3, y3, x4, y4):
    if max(x1, x2) < max(x3, x4):
        is_crossing_x = True if max(x1, x2)-min(x3, x4) >= 0 else False
        if is_crossing_x:
            x5, x6 = min(x3, x4), max(x1, x2)
    else:
        is_crossing_x = True if max(x3, x4)-min(x1, x2) >= 0 else False
        if is_crossing_x:
            x5, x6 = min(x1, x2), max(x3, x4)
    if max(y1, y2) < max(y3, y4):
        is_crossing_y = True if max(y1, y2)-min(y3, y4) >= 0 else False
        if is_crossing_y:
            y5, y6 = min(y3, y4), max(y1, y2)
    else:
        is_crossing_y = True if max(y3, y4)-min(y1, y2) >= 0 else False
        if is_crossing_y:
            y5, y6 = min(y1, y2), max(y3, y4)
    if is_crossing_y and is_crossing_x:
        s = abs(x5-x6)*abs(y5-y6)
        return True, s
    else:
        return False


all_animals = set()




