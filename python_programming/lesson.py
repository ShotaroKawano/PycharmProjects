s = 'My name is Mike. Hi Mike.'
print(s)

is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))


a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')