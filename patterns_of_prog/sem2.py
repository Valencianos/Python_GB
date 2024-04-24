#Процедурное программирование
def multiplyTo ():
    num = int(input('Enter your number: '))
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            print(f'{i} * {j} = {i * j}')

multiplyTo()

