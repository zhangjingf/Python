# _*_ coding: utf-8 _*_
classmates = ['zhang', 'jing', 'feng']
classmates.insert(3, 'today')
# print(classmates)
# t = (11, 33, 44)
# age = 3
# if age >= 18:
#     print('your age is', age)
#     print('adult')
# else:
#     print('your age is', age)
#     print('teenager')
# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
for item in classmates:
    print(item)
def my_test(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x
print(my_test(-5))
def nop():
    pass
[x*x for x in range(1, 11) if x%2 == 0]
d = {'x': 'A', 'y': 'B', 'z': 'C' }
[k + '=' + v for k, v in d.items()]