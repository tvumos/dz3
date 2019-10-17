# МОДУЛЬ 3

current_del = ","   # Разделитель элементов в строке
input_first = input("Введите элементы 1-го списка, используя разделитель запятая: ")
if current_del not in input_first:
    print("Ошибка. Не найден требуемый разделитель в списке 1. Программа завершается.")
    exit(1)

input_second = input("Введите элементы 2-го списка, используя разделитель запятая: ")
if current_del not in input_second:
    print("Ошибка. Не найден требуемый разделитель в списке 2. Программа завершается.")
    exit(2)

list_first = input_first.split(current_del)
set_first = set(list_first)
set_second = set(input_second.split(current_del))
set_result = set_first - set_second
list_result = []
for x in list_first:
    if x in set_result:
        list_result.append(x)

print(f"Результат: {current_del.join(list_result)}")
exit(0)
