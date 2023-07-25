try:
    a = float(input('Число a = '))
except ValueError:
    print('Неверный формат. Введите правильное значение')
    a = float(input('Число a = '))

action = input('Операция: ')
while (action != '+' and
    action != '-' and
    action != '*' and
    action != '/'):
    print('Не знакомая операция. Попробуйте еще раз.')
    action = input('Операция: ')

try:
    b = float(input('Число b = '))
except ValueError:
    print('Неверный формат. Введите правильное значение')
    b = float(input('Число b = '))

if action == '+':
    print(a + b)
elif action == '-':
    print(a - b)
elif action == '*':
    print(a * b)
elif action == '/':
    try:
        print(a / b)
    except ZeroDivisionError:
        print('Делить на 0 нельзя')
