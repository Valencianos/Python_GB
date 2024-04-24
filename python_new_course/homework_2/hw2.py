# 2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

import fractions
import math

str1 = '3/4'
str2 = '5/6'


def fractions_separator(num: str) -> list:
    return num.split('/')


print(fractions_separator(str1))


def fraction_methods(par1: str, par2: str) -> str:
    par1_numerator, par1_denominator = int(fractions_separator(par1)[0]), int(fractions_separator(par1)[1])
    par2_numerator, par2_denominator = int(par2[0]), int(par2[1])
    temp = lcm(par1_denominator, par2_denominator)
    res_numerator = temp // par1_denominator * par1_numerator + temp // par2_denominator * par2_numerator
    res_sum = str(res_numerator) + '/' + str(temp)
    return f'Sum of fractions {str1} and {str2} equal {res_sum}'


def lcm(num1: int, num2: int) -> int:
    return abs(num1 * num2) // math.gcd(num1, num2)


