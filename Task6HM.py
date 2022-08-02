# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.


def list_form(number: int):
    list_numbers = [(-3)**x for x in range(0, number)]
    return list_numbers


number = int(input("Enter numbers of realize function: "))
print(list_form(number))