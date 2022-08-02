# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

import os


def second_entry_find(original_lst: list, find_str: str) -> str:
    result = [i for i, v in enumerate(original_lst) if v == str(find_str)]
    if not result:
        return -1
    else:
        return (result[1])


path = os.path.join('folder', 'file4hm.txt')

with open(path, 'w') as writer:
    writer.write('qwe asd zxc qwe ertqwe')

with open(path, 'r+') as reader:
    text = reader.readline()
    str_list = [str(x) for x in text.split(' ')]
    print(f'Original text: {str_list}')
    find_str = input('Enter string to find second entry: ')
    res_index = second_entry_find(str_list, find_str)
    print(f'Finding second entry index of "{find_str}". Answer: {res_index}')
