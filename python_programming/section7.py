# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def say_something(self):
#         print('I am {}'.format(self.name))
#         self.run(10)
#
#     def run(self, num):
#         print('run' * num)
#
#     def __del__(self):
#         print('good bye')
#
#
# person = Person('Mike')
# person.say_something()
#
# del person
#
# print('############')

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self,
                 model='Model S',
                 enable_auto_run=False,
                 passwd='123'):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto run')

tesla_car = TeslaCar('Model S', passwd='456')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)
















