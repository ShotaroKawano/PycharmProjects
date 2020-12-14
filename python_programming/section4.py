r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))

print(r.count(3))

if 5 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)

# print(help(list))




i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j =', j)
print('i =', i)

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('y =', y)
print('x =', x)

print(id(x))
print(id(y))



num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

a = 100
b = 200
a,b = b,a
print(a,b)



my_friend = {'A','B','C'}
A_friend = {'B','D','F'}
print(my_friend & A_friend)

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)