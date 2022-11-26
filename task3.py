"""
3. Удвоенные нечетные.
Дано: n.

Задание: нужно получить список "удвоенных" нечетных чисел от 0 до n.

Пример:
n = 5, результат: [2, 6]
"""


def get_double_odd(n):
    array = [x*2 for x in range(0, n) if x % 2]
    return array


n = 5
print(get_double_odd(n))
