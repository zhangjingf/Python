from functools import reduce
def add(x, y):
    return x + y
reduce(add, [1, 3, 5, 7, 9]) #25
def fn(x, y):
    return x * 10 + y
reduce(fn, [1, 2, 3, 4]) #1234

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))