# 1. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны
# предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
a = int(input('Length of first side: '))
b = int(input('Length of second side: '))
c = int(input('Length of third side: '))
if (a + b > c) & (a + c > b) & (b + c > a):
    print('Triangle exist')
    if a == b == c:
        print('+ equilateral')
    elif (a == b) | (b == c) | (a == c):
        print('+ isosceles')
    else:
        print('+ versatile')
else:
    print('This is not a triangle')
