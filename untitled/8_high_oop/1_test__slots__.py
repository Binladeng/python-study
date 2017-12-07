from types import MethodType


class Student(object):
    pass


# 给student动态绑定一个属性
s = Student()
s.name = 'asd'


# 给实例动态绑定方法
def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(21)
print(s.age)


# 给实例绑定方法只对当前实例生效，需要给全部实例生效，给class绑定方法

def set_score(self, score):
    self.score = score
Student.set_score = set_score


