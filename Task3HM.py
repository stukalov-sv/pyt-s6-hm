# Найти расстояние между двумя точками пространства(числа вводятся через пробел)

import math


def is_int(input_number:str):
    try:
        input_number = int(input_number)
        return input_number
    except ValueError:
        return False


def drop_float_sign(number: float, accuracy=2) -> float:
    number = int(number * 10 ** accuracy) / 10 ** accuracy
    return number


def get_vector_length(point_a: tuple, point_b: tuple) -> int:
    res_length = math.sqrt(((point_a[0] - point_b[0])**2) + \
        ((point_a[1] - point_b[1])**2))
    return res_length


a = tuple(is_int(x) for x in input('Enter point coordinate with space - x y:').split(' '))
b = tuple(is_int(x) for x in input('Enter next point coordinate with space - x y:').split(' '))

if (False in a) or (False in b):
    print(a, b, 'Incorrect data')
else:
    print(a, b, drop_float_sign(get_vector_length(a, b)))
