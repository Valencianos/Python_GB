# 3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать
# “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
attempts = 0
while attempts < 10:
    choice = int(input('Enter number: '))
    if choice == num:
        print('My congratulations - You are the winner!')
    elif choice > num:
        print(f'{choice} is bigger than my number')
    else:
        print(f'{choice} is lower than my number')
    attempts += 1
print(f'You lost. The number was {num}')
