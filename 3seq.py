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

set_first = set(input_first.split(current_del))
set_second = set(input_second.split(current_del))
print(f"Результат: {current_del.join(set_first - set_second)}")
exit(0)
