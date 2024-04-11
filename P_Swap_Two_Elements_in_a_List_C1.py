def swapPosisions(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst

lst = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPosisions(lst, pos1-1, pos2-1))

