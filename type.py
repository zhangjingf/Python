#!/user/bin/env python3
# -*- coding: uff-8 -*-
import types

#基本类型可以用type来判断
type(13123)
type(abs)
def fn():
    pass
type(fn) == types.FunctionType
type(abs)==types.BuiltinFunctionType
type(lambda x: x)==types.LambdaType
type((x for x in range(10)))==types.GeneratorType

#判断class的类型， 使用isinstance()

dir('ABC') #dir 获取对象的所有属性和方法，返回一个包含字符串的list
len('ABC') #3
'ABC'.__len__() #3
