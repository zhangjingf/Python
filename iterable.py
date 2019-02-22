from collections import Iterable
import os
flag = isinstance('abc', Iterable) # str是否可迭代
# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)
# for x, y in [(1, 1), (2, 4), (3, 9)]:
#     print(x, y)
arr1 = list(range(1, 11))
arr2 = [x * x for x in range(1, 11)]
arr3 = [x * x for x in range(1, 11) if x % 2 == 0]
arr4 = [m + n for m in 'ABC' for n in 'XYZ']
arr5 = [d for d in os.listdir('.')]
g = (x * x for x in range(10))
# for n in g:
#     print(n)
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# fib(10)
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o  = odd()
next(o)
next(o)
next(o)
