import functools
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f())
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])) #lambda表示匿名函数，冒号前面的x表示函数参数
def build(x, y):
    return lambda: x * x + y * y
#“装饰器”（Decorator） 代码运行期间动态增加功能的方式
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')
now()
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
def int20(x, base=2):
    return int(x, base)
int21 = functools.partial(int, base=2) #偏函数