import numpy as np
from multiprocessing import Pool

def multiply_elements(args):
    i, j = args
    result = A[i][j] * B[i][j]
    # Записываем результат в промежуточный файл
    with open('matrix_C.txt', 'a') as f:
        f.write(str(result) + '\n')
    return result

# Считываем матрицы из файлов
A = np.loadtxt('matrix_A.txt')
B = np.loadtxt('matrix_B.txt')

# Проверяем, что матрицы имеют одинаковые размеры
if A.shape != B.shape:
    raise ValueError('Матрицы должны иметь одинаковые размеры')

# Создаем пул процессов
pool = Pool(processes=4)

# Вычисляем элементы матрицы-произведения в несколько потоков
C = np.zeros(A.shape)
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        C[i][j] = pool.apply_async(multiply_elements, args=((i, j),)).get()

# Записываем матрицу-произведение в файл
np.savetxt('matrix_C_final.txt', C)