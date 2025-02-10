"""
print('Text 1', 'Text 2', 'Text 3', end=' ')
print('Text 4', 'Text 5', 'Text 6')
"""

"""
print('Text 1', 'Text 2', 'Text 3', 'Text 4', 'Text 5', 'Text 6', sep='\n')
"""

"""
print('\'Text 1\'', '\'Text 2\'')
"""

"""
name = input('Введите ваше имя: ')
age = input('Введите ваш возраст: ')
print(f'Меня зовут {name}, мой возраст {age}')
"""

"""
Так делать не надо:
print('Меня зовут ', name, ', мой возраст ', age, sep='')
"""

num1 = int(input())
num2 = int(input())
print(num1 * num2)