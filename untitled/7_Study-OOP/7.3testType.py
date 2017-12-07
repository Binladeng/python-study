import types

print(type(123))
print(type('asd'))
print(type(type))


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 1.0判断某变量是否是某些变量中的一种
isinstance([1, 2, 3], (list, tuple))

# 1.1获取对象所有的方法
print(dir('asda'))
print('asd'.__len__())
print('asd'.upper())


# 1.2 配合getattr(),setattr(),hasattr() 可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print(hasattr(obj, 'x'))
setattr(obj, 'y', 15)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)

print(getattr(obj, 'z', 404))
setattr(obj, 'x', 654)
fnn = getattr(obj, 'x')
print(fnn)
