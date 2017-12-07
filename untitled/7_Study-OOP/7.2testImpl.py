class Animal(object):
    def run(self):
        print('animal is running...')


class Dog(Animal):
    def run(self):
        print('dog is running..')

    def eat(self):
        print('dog is eating...')


class Cat(Animal):
    def run(self):
        print('cat is running...')


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running...')


# python 鸭子类型 看起来像，走起来像
def run_teice(nimal):
    nimal.run()
    nimal.run()


dog = Dog()
dog.run()
dog.eat()

run_teice(Dog())

print(isinstance(dog, Cat))

cat = Cat()
cat.run()
