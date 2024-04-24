import numpy as np
np.random.seed(100)

#создать массивы из 50 случайных целых чисел от 0 до 10
var1, var2 = np.random.randint(0, 10, 50), np.random.randint(0, 10, 50)

#рассчитать корреляцию между двумя массивами
result = np.corrcoef(var1, var2)
print(result)
