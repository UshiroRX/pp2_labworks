def unique(list):
    new = []
    for i in list:
        if i not in new:
            new.append(i)
    return new

