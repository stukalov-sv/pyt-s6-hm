# Определить, присутствует ли в заданном списке строк, некоторое число

import os


def digit_check(check_str: str) -> str:
    check_list = [check_str for char in check_str if char.isdigit()]
    return (check_list)


path = os.path.join('folder', 'file1hm.txt')

with open(path, 'w') as writer:
    writer.write('Мама сшила м0не штаны и7з бере9зовой кор45ы 893.')

with open(path, 'r+') as reader:
    text = reader.readline()
    str_list = [str(x) for x in text.split(' ')]
    print(f'Original text: {str_list}')
    correct_list = [x for x in str_list if digit_check(x)]
    if not correct_list:
        print('There is no numbers in the string list elements')
    else:
        print('There is numbers in the string list elements')
    