# Найти сумму чисел списка стоящих на нечетной позиции

import random


def random_int_fill_list(size = 10) -> list:
    result_list = [random.randrange(-10, 11) for item in range(size)]
    return result_list


def odd_list_indexes_amount(user_list: list) -> int:
    index_lst = [i for i, v in enumerate(user_list)]
    result_lst = [user_list[i] for i in index_lst if i % 2 != 0]
    return (result_lst, sum(result_lst))


random_list = random_int_fill_list()
print(f'Random list:\n{random_list}')

result_list, result_amount = odd_list_indexes_amount(random_list)
print(f'Odd indexes numbers:\n{result_list}')
print(f'Odd indexes numbers amount: {result_amount}')
