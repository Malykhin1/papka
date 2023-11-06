n = int(input('Введите колличество строк: '))
my_list = []

for i in range(n):
    num = int(input('Введите значение: '))
    my_list.append(num)

print(list(reversed(my_list)))
