import math
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
L1 = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L1[0:3] #['Michael', 'Sarah', 'Tracy'] L1[:3]
