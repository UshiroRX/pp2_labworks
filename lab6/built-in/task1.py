from functools import reduce

def multiply(a):
    return reduce(lambda x,y : x*y, a)
