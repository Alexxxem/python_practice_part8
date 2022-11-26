"""
2. Перестановки.
Дано: x, y, z, n.

Задание: нужно получить список всех возможных перестановок чисел x, y, z, где x + y + z != n.

Пример:

 x = 0 y = 0 z = 1
 n = 2, результат: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""


def get_permutations(arr, n):
    result = []
    for i in arr:
        for j in arr:
            for k in arr:
                if i + j + k != n and [i, j, k] not in result:
                    result.append([i, j, k])
    return result


x = 0
y = 0
z = 1
n = 2
arr = [x, y, z]
print(get_permutations(arr, n))

