# МОДУЛЬ 1

count_item = input('Введите количество элементов: ')
while not count_item.isdigit():
    count_item = input('Повторите ввод количество элементов: ')
count_item = int(count_item)

list_item = []  # Пустой список
for index in range(1, count_item + 1):
    item = input(f'Введите {index} элемент: ')
    while not item.isdigit():
        item = input(f'Повторите ввод {index} элемента:  ')
    item = int(item)
    list_item.append(item)

list_item.sort()
print(f"Вывод: {list_item}")