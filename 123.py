# text = "hello world hello"
# print(text)
#
# text = text.replace("hello","")
# print(text)

import random
def create_list_random(list_length=10, start_number=1, end_number=10) -> list:
    new_list = []
    for _ in range(list_length):
        new_list.append(random.randint(start_number, end_number))
    return new_list
numbers = create_list_random()
print(f"Список ",numbers)

def remove_number(numbers, num_target):
    count_removed_num = numbers.count(num_target)
    if num_target in numbers = True:
        numbers = numbers.remove("num_target","")
    return count_removed_num

number_to_remove = int(input("Введіть число ", ))
removed_count = remove_number(numbers, number_to_remove)
print(f"Нова строка: ",numbers)
print(f"Кількість видалених елементів: ",removed_count)