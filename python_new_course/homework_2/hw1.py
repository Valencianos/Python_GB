# 1. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

DIV_HEX = 16
EXAMPLE = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
num: int = int(input('Enter number: '))
result: str = ''
print(f'using hex formula - {hex(num)}')
while num > 0:
    result = str(EXAMPLE[num % DIV_HEX]) + result
    num //= DIV_HEX
result = '0x' + result
print(f'manually - {result}')
