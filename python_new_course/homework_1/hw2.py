# 2. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для
# проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод
# отрицательных чисел и чисел больше 100 тысяч.
num = int(input('Enter number: '))
if num > 100000 & num < 0:
    print('Check you number!')
elif (num % 2 != 0) & (num % 3 != 0) & (num % 5 != 0) & (num % 7 != 0):
    print(f'{num} - simple number')
else:
    print(f'{num} is not so simple')
