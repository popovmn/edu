# УПРАЖНЕНИЯ ОТ 6тата ЛЕКЦИЯ за 5тата ЛЕКЦИЯ !!!

'''
#1. Jenny's Secret Message
name = input()
if name == 'Johnny':
    print('Hello, my love!')
else:
    print(f'Hello, {name}!')


#2. Drink Something
age = int(input())
kids = age <= 14
teens = age <= 18
young_adults = age <= 21
adults = age > 21
if kids:
    print('drink toddy')
elif teens:
    print('drink coke')
elif young_adults:
    print('drink beer')
elif adults:
    print('drink whisky')


#3. Leonardo DiCaprio Oscars
n = int(input())
if n == 88:
    print('Leo finally won the Oscar! Leo is happy')
elif n == 86:
    print('Not even for Wolf of Wall Street?!')
elif n != 88 or n != 86 and n < 88:
    print('When will you give Leo an Oscar?')
elif n > 88:
    print('Leo got one already!')


#4.
word = input()
doubled_word = ''
for i in word:
    doubled_word = i + i
    print(doubled_word, end='')


#5.
n_sheeps = int(input())
for i in range(1, n_sheeps+1):
    print(f'{i} sheep...', end='')

#6.



#7.
divider = int(input())
num_ = int(input())
result = 0
for i in range(num_, 1, -1):
    if i % divider == 0:
        result = i
        break
print(result)


#8.


#9.


# 10 - НЕДОВЪРШЕНА
quantity = int(input('Quantity: '))
days = int(input('Days: '))
ORNAMENT_SET = 2
TREE_SKIRT = 5
TREE_GARLANDS = 3
TREE_LIGHTS = 15
christmas_spirit = 0
total_sum = 0

for i in range(1, days + 1):  # OK
    if i % 1 == 1:
        total_sum = ORNAMENT_SET + TREE_SKIRT + TREE_GARLANDS + TREE_LIGHTS
        print(total_sum)


### ?
command = input()
coffee = 0
count = 1

while command not in ["END", "end"]:

    if command in ["coding", "dog", "cat", "movie"]:
        coffee += 1
    elif command in ["CODING", "DOG", "CAT", "MOVIE"]:
        coffee += 2

    command = input()
    count += 1

if count > 5:
    print("You need extra sleep")
else:
    print(coffee)








'''

