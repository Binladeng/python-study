stud1 = {'anme': 'zhangsan', 'age': 12}
stud2 = {'name': 'lisi', 'age': 32}


def print_age(std):
    print('%s: %s' % (std['name'], std['age']))


class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_age(self):
        print('name:%s\nage:%s' % (self.age, self.__name))

    def get_age(self):
        if self.age > 50:
            return 'old'
        elif self.age < 20:
            return 'little'
        else:
            return 'mid'

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name == name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 0 <= age <= 100:
            self.__age = age
        else:
            raise ValueError('baaaaaaaaaaaaaaaaad')


wangwu = Student('wangwu', 21)
print(wangwu.age, wangwu.get_age())
lisa = Student('lisa', 65)

wangwu.print_age()
bart = Student('bart', 32)
bart.name = 'asdasd'
print(bart.name)
