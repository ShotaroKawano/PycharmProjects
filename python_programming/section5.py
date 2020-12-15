is_empty = None

if is_empty is None:
    print('None!')

count = 0

while count < 5:
    print(count)
    count += 1
else:
    print('done')

# while True:
#     word = input('Enter:')
#     if word == 'ok':
#         break
#     print('next')

some_list = [1, 2, 3, 4, 5]

for i in some_list:
    print(i)

for _ in range(2, 10, 3):
    print('hello')

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

d = {'x': 100, 'y': 200}

print(d.items())
for k, v in d.items():
    print(k, ':', v)

def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func(100)
print(r)
r = test_func(100)
print(r)


def say_something(word, *args):
    print('word =', word)
    print('args =', args)
    for arg in args:
        print(arg)

say_something('Hi!', 'Mike', 'Nacy')

# t = ('Hi!', 'Mike')
# say_something('Hi!', *t)

def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice',
}
menu(**d)

def menu2(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu2('banana', 'apple', 'orange', entree="beef", drink='coffee')

def example_func(param1, param2):
    """Example function with types document in the docstring.

    :param param1: (int) The first parameter.
    :param param2: (int) The second parameter.
    :return: (bool) The return value. True for success, False otherwise.
    """
    print(param1)
    print(param2)
    return True

print(example_func.__doc__)
help(example_func)


def outer(a, b):
    def inner():
        return a + b
    return inner

f = outer(1, 2)
r = f()
print(r)


def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
def add_num(a, b):
    return a + b

# f = print_info(add_num)
# r = f(10, 20)
# print(r)

r = add_num(10, 20)
print(r)

l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# sample_func = lambda word:word.capitalize()
change_words(l, lambda word:word.capitalize())



def counter(num=10):
    for _ in range(num):
        yield 'run'

def greeting():
    yield 'Good morning'
    # for i in range(1000000):
    #     print(i)
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
c = counter()

print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(g))



t = (1, 2, 3, 4, 5)
r = [i for i in t]
s = [i for i in t if i % 2 == 0]
print(r)
print(s)

w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']
d = {x: y for x, y in zip(w, f)}
print(d)

s = {i for i in range(10) if i % 2 == 0}
print(s)

g = (i for i in range(10))
print(type(g))
g = tuple(i for i in range(10))
print(type(g))



animal = 'cat'

def f():
    global animal
    animal = 'dog'
    print('local', animal)

f()
print('global', animal)
print('global:', globals())



l = [1, 2, 3]
i = 5
try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
else:
    print('done')
finally:
    print('clean up')



class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

check()