# МОДУЛЬ 2

delimiters = [",", ";", "/"]
input_str = input(f'Введите элементы списка, используя один из следующих разделителей ({" ".join(delimiters)}): ')

current_del = ""    # Разделитель указанный пользователем в строке
for temp_del in delimiters:
    if temp_del in input_str:
        if current_del == "":
            current_del = temp_del
        else:
            print(f"Ошибка. Во введённой строке Вы указали несколько разделителей {current_del} и {temp_del}")
            print("Ошибка. Необходимо указать один разделитель элементов. Программа завершается.")
            exit(1)

if (current_del == ""):
    print(f"Ошибка. Не найден один из допустимых разделителей {' '.join(delimiters)}. Программа завершается.")
    exit(2)

result_list = []    # Выходной список
temp_list = input_str.split(current_del)
for i in temp_list:
    if temp_list.count(i) == 1:
        result_list.append(i)

print(f"Результат: {current_del.join(result_list)}")
exit(0)
