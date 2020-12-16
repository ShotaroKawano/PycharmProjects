# import sys

# print(sys.argv)
# for i in sys.argv:
#     print(i)

# import lesson_package.utils
# from lesson_package.tools import utils

# from lesson_package.utils import say_twice

# r = utils.say_twice('hello')

# print(r)


# from lesson_package.talk import human
# from lesson_package.talk import animal
# from lesson_package.talk import *

# print(human.sing())
# print(human.cry())
# print(animal.sing())
# print(animal.cry())

# try:
#     from lesson_package import utils
# except ImportError:
#     from lesson_package.tools import utils
#
# utils.say_twice('word')



# print(globals())
# import builtins
#
# builtins.print('builtins')
#
# ranking = {
#     'A': 100,
#     'B': 85,
#     'C': 95
# }
#
# print(sorted(ranking, key=ranking.get, reverse=True))
#
#
#
# s = 'fdglaglsdkflaskfsa'
#
# d = {}
# for c in s:
#     if c not in d:
#         d[c] = 0
#     d[c] += 1
# print(d)
#
# d = {}
# for c in s:
#     d.setdefault(c, 0)
#     d[c] += 1
# print(d)
#
# from collections import defaultdict
#
# d = defaultdict(int)
#
# for c in s:
#     d[c] += 1
# print(d)
#
#
#
# from termcolor import colored
#
# print('test')
# print(colored('test', 'red'))
# print(colored('test', 'red', 'on_grey'))
#
# print(help(colored))
#
#
#
# import collections
# import os
# import sys
#
# import termcolor
#
# import lesson_package
#
# import config
#
# print(collections.__file__)
# print(termcolor.__file__)
#
# print(sys.path)



import lesson_package.talk.animal
import config

def main():
    lesson_package.talk.animal.sing()

if __name__ == '__main__':
    main()

# print(__name__)
