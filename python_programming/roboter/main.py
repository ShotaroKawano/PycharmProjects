import csv
import os
import string

def say():
    with open('template/greeting.txt') as f:
        t = string.Template(f.read())
        content = t.substitute()

    print(content)


def say2(restaurant_name):
    with open('template/ask_wether.txt') as f:
        t = string.Template(f.read())
        content = t.substitute(restaurant_name=restaurant_name)

    print(content)


def say3(user_name):
    with open('template/ask_restaurant.txt') as f:
        t = string.Template(f.read())
        content = t.substitute(user_name=user_name)

    print(content)


def say4(user_name):
    with open('template/goodbye.txt') as f:
        t = string.Template(f.read())
        content = t.substitute(user_name=user_name)

    print(content)


def wirteCsv(name, count):
    with open('recommend.csv', 'w') as csv_file:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Name': name, 'Count': count})

def readCsv():
    restaurant_list = dict()
    with open('recommend.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            restaurant_list[row['Name']] = row['Count']
        print(restaurant_list)
    return restaurant_list


say()
word = ''
while True:
    word = input('Enter:')
    if word == '':
        print('入力は必須です。')
    else:
        user_name = word
        break

if os.path.exists('recommend.csv'):
    while True:
        say2('apple')
        word = ''
        while True:
            word = input('Enter:')
            if word == '':
                print('入力は必須です。')
            else:
                break
        break

say3(user_name)
word = ''
while True:
    word = input('Enter:')
    if word == '':
        print('入力は必須です。')
    else:
        restaurant_name = word
        wirteCsv(restaurant_name, 1)
        break


say4(user_name)
readCsv()

