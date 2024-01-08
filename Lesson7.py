# Завдання 1
# Напишіть функцію, яка обчислює добуток елементів списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.
#
# Завдання 2
# Напишіть функцію для знаходження мінімуму у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.
#
# Завдання 3
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.
#
# Завдання 4
# Напишіть функцію, яка видаляє зі списку ціле задане число.
# З функції потрібно повернути кількість видаленних елементів.
#
# Завдання 5
# Напишіть функцію, яка отримує два списки як параметр і повертає список,
# що містить елементи обох списків.
#
# Завдання 6
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список також передається як параметр.
# Функція повертає новий список, який містить отримані результати.

# Завдання 1
# Напишіть функцію, яка обчислює добуток елементів списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

import random
def create_list_random(list_length=10, start_number=1, end_number=10) -> list:
    new_list = []
    for _ in range(list_length):
        new_list.append(random.randint(start_number, end_number))
    return new_list
numbers = create_list_random()
print(f"Список ",numbers)
def mult(numbers):
    mult = 1
    for i in range(len(numbers)):
        mult *= numbers[i]
    return mult
multi = mult(numbers)
print(f"Добуток елементів списку ",multi)

# Завдання 2
# Напишіть функцію для знаходження мінімуму у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

import random
def create_list_random(list_length=10, start_number=1, end_number=10) -> list:
    new_list = []
    for _ in range(list_length):
        new_list.append(random.randint(start_number, end_number))
    return new_list
numbers = create_list_random()
print(f"Список ",numbers)
def find_min(numbers):
    min_number = min(numbers)
    return min_number
result_min = find_min(numbers)
print(f"Мінімум ",result_min)
