n = int(input('Введите количество символов: '))
my_list = []

for i in range(n):
    element = input('Введите элементы списка: ')
    my_list.append(element)

print(*my_list)

for my_l in my_list:
    print(my_l)