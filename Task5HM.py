# Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
import math

def random_int_fill_list(size = 10) -> list:
    result_list = [random.randrange(-10, 11) for item in range(size)]
    return result_list

def pair_numbers_multiply(user_list: list) -> list:
    reverse_user_list = [i for i in reversed(user_list)]
    result_list_multiply = [user_list[i] * reverse_user_list[i] for i, v in enumerate(user_list) \
                            if i <= math.ceil(len(user_list) // 2)]
    return result_list_multiply

random_list = random_int_fill_list(int(input('Enter list length: ')))
print(f'Random list:\n{random_list}')
print(f'Multiply numbers list:\n{pair_numbers_multiply(random_list)}')
